def get_brazil_date_from_string(date):
    month_br = {
        1: 'Janeiro',
        2: 'Fevereiro',
        3: 'Março',
        4: 'Abril',
        5: 'Maio',
        6: 'Junho',
        7: 'Julho',
        8: 'Agosto',
        9: 'Setembro',
        10: 'Outubro',
        11: 'Novembro',
        12: 'Dezembro'
    }
    day, month, year = date.split("/")
    return '%s de %s de %s' % (day, month_br[int(month)], year)