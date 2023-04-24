def number_of_followers(id, api):
    user = api.get_user(user_id=str(id))
    return user.followers_count


def tweet(info, api):
    api.update_status(status=info)
