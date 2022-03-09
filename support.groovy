def set_assignee(login) // логин сотрудника поддержки
{
	// request_data - интерфейс управления БД. Считать, что не может исполняться несколько операций с БД параллельно
	requests = request_data.get_all() // получаем все обращения пользователей из БД
	// Предположу, что проблема в использовании метода collect{ key, value -> value.max{ it.version }
	// Использование вместо него findAll{ key, value -> value.max{ it.version } должно помочь
	request = requests.groupBy{
		it.id
	}.findAll{ key, value ->
		value.max{ it.version }
	}.findAll{ req ->
		req.status == 'opened' &&
		req.state == 'ready'
	}.max{
		it.priority
	}
	if (request == null)
		return null

	request.state = 'inprogress'
	request.assignee = login
	request.version += 1
	request_data.upload(request) // загружаем новую версию обращения в БД (старая не удаляется)
	return request
}
