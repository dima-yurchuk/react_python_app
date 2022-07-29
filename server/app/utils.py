def hundleResult(users):
    users_list=[]
    for user in users:
        users_list.append({'id': user.id, 'end_user_id': user.end_user_id, 'web_page_url':user.web_page_url})
    return users_list