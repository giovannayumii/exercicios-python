print("Faça um programa para o curso de ADS (6 módulos) que calcule e apresente os seguintes itens:")
print("Quantidade de homens e mulheres de cada módulo;\tMédia de idades de cada módulo;\tQuantidade de homens e mulheres do curso todo;\tMédia de idades do curso todo.")

x = 0
contm_curso = 0
contf_curso = 0
somaf_curso = 0
somam_curso = 0
for modulo in range(1, 3):
    contm = 0
    contf = 0
    somam_modulo = 0
    somaf_modulo = 0
    n = int(input('Informe a quantidade de alunos: '))
    for x in range(n):
        sexo = input('Informe o sexo do aluno: ')
        idade = int(input('Informe a idade do aluno: '))
        if sexo == 'm' or sexo == 'M':
            contm += 1
            somam_modulo += idade
            contm_curso +=1
            somam_curso += idade
        elif sexo == 'f' or sexo == 'F':
            contf += 1
            somaf_modulo += idade
            contf_curso += 1
            somaf_curso += idade
        media_modulo = (somam_modulo + somaf_modulo) / (contm + contf)
        media_curso = (somam_curso + somaf_curso) / (contm_curso + contf_curso)
    
    print('A quantidade de homens do ',modulo,'º módulo é de',contm,' homens')
    print('A quantidade de mulheres do',modulo,'º módulo é de',contf,'mulheres')
    print('A média de idade entre os alunos do ',modulo,'º módulo é de', media_modulo,' anos')
    
print('A quantidade de homens de todo o curso é de',contm_curso,'homens')
print('A quantidade de mulheres de todo o curso é de',contf_curso,' mulheres')
print('A média de idade entre os alunos de todo o curso é de ',media_curso,' anos')