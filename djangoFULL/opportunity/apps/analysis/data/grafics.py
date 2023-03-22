from project.models import vagasEmprego


class Start:
    def define_data_info(data: dict):
        data['alunos_SI_pesquisa'] = 0
        data['alunos_LCC_pesquisa'] = 0

        data['inscricoes_SI_pesquisa'] = 0
        data['inscricoes_LCC_pesquisa'] = 0

        data['alunos_SI_extensao'] = 0
        data['alunos_LCC_extensao'] = 0

        data['inscricoes_SI_extensao'] = 0
        data['inscricoes_LCC_extensao'] = 0

        data['alunos_SI_estagio'] = 0
        data['alunos_LCC_estagio'] = 0

        data['inscricoes_SI_estagio'] = 0
        data['inscricoes_LCC_estagio'] = 0

        return data

    def define_info_count_from_jobs(data: dict):
        data['PP'] = vagasEmprego.objects.filter(tipo_vaga='PP').count()
        data['PE'] = vagasEmprego.objects.filter(tipo_vaga='PE').count()
        data['ES'] = vagasEmprego.objects.filter(tipo_vaga='ES').count()

        return data

    def query_set_info_from_jobs(query_set_data: dict):
        query_set_data['queryset_pesquisa'] = vagasEmprego.objects.filter(
            tipo_vaga='PP')
        query_set_data['queryset_extensao'] = vagasEmprego.objects.filter(
            tipo_vaga='PE')
        query_set_data['queryset_estagio'] = vagasEmprego.objects.filter(
            tipo_vaga='ES')

        return query_set_data

    def cal_info_students_in_extension_project(query_set_data: dict, alunos_extensao: list, data: dict):
        for extensao in query_set_data['queryset_extensao']:
            for aluno in extensao.aluno.values().distinct():
                if aluno['curso'] == 'SI' and aluno not in alunos_extensao:
                    alunos_extensao.append(aluno)
                    data['alunos_SI_extensao'] += 1
                elif aluno['curso'] == 'LCC' and aluno not in alunos_extensao:
                    alunos_extensao.append(aluno)
                    data['alunos_LCC_extensao'] += 1

        return {
            'alunos_extensao': alunos_extensao,
            'data': data
        }

    def all_subscribe_in_extesion_project(query_set_data: dict, alunos_extensao: list, data: dict):
        for extensao in query_set_data['queryset_extensao']:
            for aluno in extensao.aluno.values().distinct():
                if aluno['curso'] == 'SI':
                    data['inscricoes_SI_extensao'] += 1
                elif aluno['curso'] == 'LCC':
                    data['inscricoes_LCC_extensao'] += 1

        return {
            'data': data
        }

    def cal_info_stundents_in_research_project(query_set_data: dict, alunos_pesquisa: list, data: dict):
        for pesquisa in query_set_data['queryset_pesquisa']:
            for aluno in pesquisa.aluno.values().distinct():
                if aluno['curso'] == 'SI' and aluno not in alunos_pesquisa:
                    alunos_pesquisa.append(aluno)
                    data['alunos_SI_pesquisa'] += 1
                if aluno['curso'] == 'LCC' and aluno not in alunos_pesquisa:
                    alunos_pesquisa.append(aluno)
                    data['alunos_LCC_pesquisa'] += 1

        return {
            'alunos_pesquisa': alunos_pesquisa,
            'data': data
        }

    def all_subscribe_in_research_project(query_set_data: dict, alunos_pesquisa: list, data: dict):
        for pesquisa in query_set_data['queryset_pesquisa']:
            for aluno in pesquisa.aluno.values().distinct():
                if aluno['curso'] == 'SI':
                    data['inscricoes_SI_pesquisa'] += 1
                if aluno['curso'] == 'LCC':
                    data['inscricoes_LCC_pesquisa'] += 1

        return {
            'data': data
        }

    def cal_info_students_in_intern(query_set_data: dict, alunos_estagio: list, data: dict):
        for estagio in query_set_data['queryset_estagio']:
            for aluno in estagio.aluno.values().distinct():
                if aluno['curso'] == 'SI' and aluno not in alunos_estagio:
                    alunos_estagio.append(aluno)
                    data['alunos_SI_estagio'] += 1
                elif aluno['curso'] == 'LCC' and aluno not in alunos_estagio:
                    alunos_estagio.append(aluno)
                    data['alunos_LCC_estagio'] += 1

        return {
            'alunos_estagio': alunos_estagio,
            'data': data
        }

    def all_subscribe_in_intern(query_set_data: dict, alunos_estagio: list, data: dict):
        for estagio in query_set_data['queryset_estagio']:
            for aluno in estagio.aluno.values().distinct():
                if aluno['curso'] == 'SI':
                    data['inscricoes_SI_estagio'] += 1
                if aluno['curso'] == 'LCC':
                    data['inscricoes_LCC_estagio'] += 1

        return {
            'data': data
        }


class IndividualStart:
    def define_data_info(data: dict):
        data['alunos_SI'] = 0
        data['alunos_LCC'] = 0

        data['inscricoes_SI'] = 0
        data['inscricoes_LCC'] = 0

        return data

    def define_info_count_from_jobs(data: dict, vaga_id: int):
        data['vagas'] = vagasEmprego.objects.filter(
            id=vaga_id).values('numeroVagas')
        data['vagas'] = data['vagas'][0]['numeroVagas']
        data['vaga_object'] = vagasEmprego.objects.filter(
            id=vaga_id)

        return data

    def info_subscribe_in_job(data: dict, alunos: list):
        query_set_data = data['vaga_object']

        for alunos_curso in query_set_data:
            for aluno in alunos_curso.aluno.values().distinct():
                if aluno['curso'] == 'SI' and aluno not in alunos:
                    alunos.append(aluno)
                    data['alunos_SI'] += 1
                elif aluno['curso'] == 'LCC' and aluno not in alunos:
                    alunos.append(aluno)
                    data['alunos_LCC'] += 1

        return {
            'alunos': alunos,
            'data': data
        }

    # def all_subscribe_in_job(data: dict):
    #     query_set_data = data['vaga_object']

    #     for info in query_set_data:
    #         for aluno in info.aluno.values().distinct():
    #             if aluno['curso'] == 'SI':
    #                 data['inscricoes_SI'] += 1
    #             elif aluno['curso'] == 'LCC':
    #                 data['inscricoes_LCC'] += 1

    #     return {
    #         'data': data
    #     }

        pass
