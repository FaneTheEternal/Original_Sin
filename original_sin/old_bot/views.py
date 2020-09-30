from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

import vk_api
from vk_api.exceptions import ApiError

from . import chat_bot
from .models import VkUser

import json
import sys


@csrf_exempt
def index(request):
    token = getattr(settings, 'CHUVSU_VK_TOKEN')
    secret_key = getattr(settings, 'CHUVSU_VK_SECRET_KEY')
    confirmation_token = getattr(settings, 'CHUVSU_VK_CONFIRMATION_TOKEN')

    if request.method == "POST":
        data = json.loads(request.body)
        if data['secret'] == secret_key:
            if data['type'] == 'confirmation':
                return HttpResponse(
                    confirmation_token,
                    content_type="text/plain",
                    status=200
                    )
            if data['type'] == 'message_new':
                try:
                    print(request.method, file=sys.stderr)
                    print(request.body, file=sys.stderr)
                    chat_bot.execute(data)
                except Exception as e:
                    print(e, file=sys.stderr)
            if data['type'] == 'message_reply':
                vk_session = vk_api.VkApi(token=token)
                vk = vk_session.get_api()
                obj = data['object']
                text = obj['text']
                if text == '!Начать':
                    message_ids = obj['id']
                    spam = int(False)
                    group_id = data['group_id']
                    delete_for_all = int(True)
                    peer_id = obj['peer_id']
                    try:
                        vk.messages.delete(
                            message_ids=message_ids,
                            spam=spam,
                            group_id=group_id,
                            delete_for_all=delete_for_all,
                        )
                    except ApiError as pezdos:
                        print('message_ids: ', message_ids, file=sys.stderr)
                        print('group_id: ', group_id, file=sys.stderr)
                        print('delete_for_all: ', delete_for_all, file=sys.stderr)
                        print('Pezdos: ', pezdos, file=sys.stderr)
                    else:
                        user, _ = VkUser.objects.get_or_create(user_id=peer_id)
                        chat_bot.go_home(vk, user)
            return HttpResponse(
                    'ok',
                    content_type="text/plain",
                    status=200
                    )
    else:
        return HttpResponse('see you :)')


@csrf_exempt
def fill(request):
    response = 'got ' + request.method
    if request.method == 'POST':
        try:
            data = request.POST.copy()
            data = dict(data)
            data = data.get('data')
            data = data[0]
            data = data.split()
            data = ((i.split(':')) for i in data)
            data = dict(data)
            bulk = []
            for user_id, status in data.items():
                obj = VkUser(user_id=user_id, status=status)
                bulk.append(obj)
            VkUser.objects.bulk_create(bulk, batch_size=100)
        except Exception as e:
            response += f' {e}'
        else:
            response += ' <created>'
    return HttpResponse(response)


def raw(request):
    qs = VkUser.objects.all()
    ids = ['{id}:{status}'.format(id=i.user_id, status=i.status) for i in qs]
    result = ' '.join(ids)
    return HttpResponse(result)
