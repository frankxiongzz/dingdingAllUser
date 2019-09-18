from dingtalk import SecretClient

def get_all_user_by_departments(client, all_departments):

    if all_departments is None:
        return
    else:
        for department in all_departments:
            # 打印该部门的成员
            userList = client.user.simple_list(department_id = department['id'])
            for user in userList['userlist']:
                print(user)

            # 递归下去
            all_child_departments = client.department.list(department['id'])
            get_all_user_by_departments(client, all_child_departments)

if __name__ == '__main__':

    CORP_ID = "xxxxxx"
    APPKEY = "xxxxxxxxxx"
    SECRET = "xxxxxxxxxx"
    AGENT_ID = "xxxxx"
    client = SecretClient(APPKEY, SECRET)

    all_departments = client.department.list()
    get_all_user_by_departments(client, all_departments)
