from django.shortcuts import render, redirect


def get_boards_data():
    """Вспомогательная функция для получения данных всех досок"""
    return {
        'dormitories': [
            {'slug': 'd1', 'name': 'Общежитие №1'},
            {'slug': 'd2', 'name': 'Общежитие №2'},
            {'slug': 'd3', 'name': 'Общежитие №3'},
            {'slug': 'd4', 'name': 'Общежитие №4'},
            {'slug': 'd6', 'name': 'Общежитие №6'},
            {'slug': 'd7', 'name': 'Общежитие №7'},
            {'slug': 'd8', 'name': 'Общежитие №8'},
            {'slug': 'd9-1', 'name': 'Общежитие №9/1'},
            {'slug': 'd9-2', 'name': 'Общежитие №9/2'},
            {'slug': 'd11', 'name': 'Общежитие №11'},
        ],
        'institutes': [
            {'slug': 'iibat', 'name': 'ИБЭАТ'},
            {'slug': 'iiya', 'name': 'ИИЯ'},
            {'slug': 'ippisn', 'name': 'ИППиСН'},
            {'slug': 'ilgisn', 'name': 'ИЛГиСН'},
            {'slug': 'imit', 'name': 'ИМИТ'},
            {'slug': 'ipp', 'name': 'ИПП'},
            {'slug': 'ifkisit', 'name': 'ИФКиСит'},
            {'slug': 'if', 'name': 'ИФ'},
            {'slug': 'iep', 'name': 'ИЭП'},
            {'slug': 'mi', 'name': 'МИ'},
            {'slug': 'fti', 'name': 'ФТИ'},
        ],
        'buildings': [
            {'slug': 'b12', 'name': 'Главный учебный корпус'},
            {'slug': 'b13', 'name': 'Теоретический корпус'},
            {'slug': 'b14', 'name': 'Морфологический корпус'},
            {'slug': 'b1', 'name': 'Учебный корпус №1'},
            {'slug': 'b2', 'name': 'Учебный корпус №2'},
            {'slug': 'b3', 'name': 'Учебный корпус №3'},
            {'slug': 'b4', 'name': 'Учебный корпус №4'},
            {'slug': 'b5', 'name': 'Учебно-лабораторный корпус №5'},
            {'slug': 'b6', 'name': 'Учебно-лабораторный корпус №6'},
            {'slug': 'b7', 'name': 'Учебный корпус №7'},
            {'slug': 'b8', 'name': 'Учебный корпус №8'},
            {'slug': 'b9', 'name': 'Учебный корпус №9'},
            {'slug': 'b10', 'name': 'Учебный корпус №10'},
            {'slug': 'b11', 'name': 'Учебно-лабораторный корпус №11'},
        ],
        'misc_list': [
            {'slug': 'm1', 'name': 'Преподаватели'},
            {'slug': 'm2', 'name': 'Расписание'},
            {'slug': 'm3', 'name': 'Военная кафедра'},
            {'slug': 'm4', 'name': 'Столовые и еда'},
            {'slug': 'm5', 'name': 'Студенческие объединения'},
            {'slug': 'm6', 'name': 'Спорт и секции'},
            {'slug': 'm7', 'name': 'Мероприятия'},
            {'slug': 'm8', 'name': 'Флуд и мемы'},
            {'slug': 'm9', 'name': 'Потерянные вещи'},
        ]
    }


def home(request):
    # Используем общую функцию для получения данных досок
    context = get_boards_data()
    return render(request, 'main/home.html', context)

def thread_list(request, board_slug):
    # Простой мок для примера — потом заменим на реальные данные из БД
    sample_threads = [
        {
            "id": 1,
            "author": "Аноним",
            "date": "12.01.2025",
            "weekday": "Понедельник",
            "time": "14:22",
            "title": "Названия_треда1",
            "image": None,  # или путь к файлу
            "text": "Все треды сбоку кликабельны и переносят на отдельную страницу треда ес чо ...",
        },
        {
            "id": 2,
            "author": "Анон",
            "date": "12.01.2025",
            "weekday": "Понедельник",
            "time": "15:41",
            "title": "Название_треда2",
            "image": None,
            "text": "Другой текст другого треда..." * 3,
        }
    ]

    # Получаем данные досок из общей функции
    boards_data = get_boards_data()
    dormitories = boards_data['dormitories']
    institutes = boards_data['institutes']
    buildings = boards_data['buildings']
    misc_list = boards_data['misc_list']

    # Определяем название доски по slug
    board_titles = {}
    # Добавляем все доски из списков
    for dorm in dormitories:
        board_titles[dorm['slug']] = dorm['name']
    for inst in institutes:
        board_titles[inst['slug']] = inst['name']
    for building in buildings:
        board_titles[building['slug']] = building['name']
    for item in misc_list:
        board_titles[item['slug']] = item['name']
    
    board_title = board_titles.get(board_slug, f"Раздел: {board_slug}")

    return render(
        request,
        "main/thread_list.html",
        {
            "board_slug": board_slug,
            "board_title": board_title,
            "threads": sample_threads,
            "dormitories": dormitories,
            "institutes": institutes,
            "buildings": buildings,
            "misc_list": misc_list,
        }
    )


def thread_detail(request, board_slug, thread_id):
    """Страница отдельного треда с ответами"""
    # Моковые данные тредов для демонстрации
    threads_data = {
        1: {
            "id": 1,
            "author": "Аноним",
            "date": "12.01.2025",
            "weekday": "Понедельник",
            "time": "14:22",
            "title": "Названия_треда1",
            "image": None,
            "text": "Все треды сбоку кликабельны и переносят на отдельную страницу треда ес чо ...",
        },
        2: {
            "id": 2,
            "author": "Анон",
            "date": "12.01.2025",
            "weekday": "Понедельник",
            "time": "15:41",
            "title": "Название_треда2",
            "image": None,
            "text": "Другой текст другого треда..." * 3,
        },
    }
    
    # Моковые данные ответов
    replies_data = {
        1: [
            {
                "id": 101,
                "author": "Аноним",
                "date": "12.01.2025",
                "weekday": "Понедельник",
                "time": "14:45",
                "text": "Отличный тред! Полностью согласен с автором.",
                "image": None,
            },
            {
                "id": 102,
                "author": "Анон",
                "date": "12.01.2025",
                "weekday": "Понедельник",
                "time": "15:10",
                "text": "А я не согласен. Вот почему: текст текст текст...",
                "image": None,
            },
            {
                "id": 103,
                "author": "Аноним",
                "date": "12.01.2025",
                "weekday": "Понедельник",
                "time": "16:20",
                "text": "Тоже считаю, что это важная тема для обсуждения.",
                "image": None,
            },
        ],
        2: [
            {
                "id": 201,
                "author": "Аноним",
                "date": "12.01.2025",
                "weekday": "Понедельник",
                "time": "16:00",
                "text": "Интересная тема. Поддерживаю автора.",
                "image": None,
            },
        ],
    }
    
    # Получаем данные досок
    boards_data = get_boards_data()
    dormitories = boards_data['dormitories']
    institutes = boards_data['institutes']
    buildings = boards_data['buildings']
    misc_list = boards_data['misc_list']
    
    # Определяем название доски
    board_titles = {}
    for dorm in dormitories:
        board_titles[dorm['slug']] = dorm['name']
    for inst in institutes:
        board_titles[inst['slug']] = inst['name']
    for building in buildings:
        board_titles[building['slug']] = building['name']
    for item in misc_list:
        board_titles[item['slug']] = item['name']
    
    board_title = board_titles.get(board_slug, f"Раздел: {board_slug}")
    
    # Получаем данные треда и ответов
    thread = threads_data.get(thread_id)
    replies = replies_data.get(thread_id, [])
    
    if not thread:
        from django.http import Http404
        raise Http404("Тред не найден")
    
    return render(request, 'main/thread_detail.html', {
        "board_slug": board_slug,
        "board_title": board_title,
        "thread": thread,
        "replies": replies,
        "dormitories": dormitories,
        "institutes": institutes,
        "buildings": buildings,
        "misc_list": misc_list,
    })


def login_view(request):
    """Страница входа для модераторов/администраторов"""
    error = None
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Простая проверка (пока без БД)
        # В реальном приложении здесь будет проверка через Django authentication
        if username == 'u' and password == 'p':
            # Временная логика для демонстрации
            # TODO: подключить Django authentication для реальной проверки
            # Пока просто редиректим на главную при заполненных полях
            return redirect('home')
        else:
            error = 'Пожалуйста, заполните все поля'
    
    return render(request, 'main/login.html', {'error': error})


def rules_view(request):
    """Страница с правилами использования сайта"""
    return render(request, 'main/rules.html')


def reports_view(request):
    """Страница с жалобами для модераторов/администраторов"""
    # Моковые данные жалоб (в реальном приложении будут из БД)
    thread_complaints = [
        {
            'id': 1,
            'thread_title': 'Обсуждение расписания',
            'board_slug': 'iibat',
            'board_name': 'ИБЭАТ',
            'date': '12.01.2025 14:30',
            'reason': 'Содержит оскорбления в адрес преподавателя',
            'type': 'thread',
        },
        {
            'id': 2,
            'thread_title': 'Вопрос про сессию',
            'board_slug': 'd1',
            'board_name': 'Общежитие №1',
            'date': '11.01.2025 18:22',
            'reason': 'Спам и флуд',
            'type': 'thread',
        },
    ]

    message_complaints = [
        {
            'id': 3,
            'thread_title': 'Реп по матану',
            'board_slug': 'mit',
            'board_name': 'МИ',
            'date': '10.01.2025 10:15',
            'reason': 'Распространение личных данных',
            'type': 'message',
        },
        {
            'id': 4,
            'thread_title': 'Лабы по программированию',
            'board_slug': 'imit',
            'board_name': 'ИМИТ',
            'date': '09.01.2025 16:45',
            'reason': 'пидорас он',
            'type': 'message',
        },
    ]

    # Определяем выбранную жалобу из GET параметров
    selected_type = request.GET.get('type', '')
    selected_id = request.GET.get('id')
    selected_complaint = None

    if selected_id:
        try:
            selected_id = int(selected_id)
            if selected_type == 'thread':
                for complaint in thread_complaints:
                    if complaint['id'] == selected_id:
                        selected_complaint = complaint
                        break
            elif selected_type == 'message':
                for complaint in message_complaints:
                    if complaint['id'] == selected_id:
                        selected_complaint = complaint
                        break
        except ValueError:
            pass

    return render(request, 'main/reports.html', {
        'thread_complaints': thread_complaints,
        'message_complaints': message_complaints,
        'selected_complaint': selected_complaint,
        'selected_id': selected_id,
        'selected_type': selected_type,
    })


def settings_view(request):
    """Страница настроек сайта для модераторов/администраторов"""
    # В реальном приложении слова будут храниться в БД
    # Для демонстрации используем сессию
    if 'banned_words' not in request.session:
        request.session['banned_words'] = ['мат', 'спам', 'флуд']
    
    # Создаем копию списка для работы
    banned_words = list(request.session['banned_words'])
    error = None
    success = None
    
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'add':
            word = request.POST.get('word', '').strip().lower()
            if word:
                if word not in banned_words:
                    banned_words.append(word)
                    request.session['banned_words'] = banned_words
                    request.session.modified = True
                    success = f'Слово "{word}" добавлено в список запрещенных'
                else:
                    error = f'Слово "{word}" уже есть в списке'
            else:
                error = 'Пожалуйста, введите слово'
        
        elif action == 'remove':
            word = request.POST.get('word', '').strip().lower()
            if word and word in banned_words:
                banned_words.remove(word)
                request.session['banned_words'] = banned_words
                request.session.modified = True
                success = f'Слово "{word}" удалено из списка'
            else:
                error = 'Слово не найдено в списке'
    
    return render(request, 'main/settings.html', {
        'banned_words': sorted(banned_words),
        'error': error,
        'success': success,
    })