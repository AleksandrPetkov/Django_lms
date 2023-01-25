def format_list_students(students):
    string = '<table><thead><tr><th>First name</th><th>Last name</th><th>Email</th><th>Birthday</th></tr><thead><tbody>'
    for st in students:
        string += f'<tr><td>{st.first_name}</td><td>{st.last_name}</td><td>{st.email}</td><td>{st.birthday}</td></tr>'
    string += '</tbody></table>'
    return string


def normalize_phone(value):
    chars = '1234567890()+-'
    result = ''
    for char in value:
        if char in chars:
            result += char
    return result

