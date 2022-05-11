# | pipe 
import re
batRegex = re.compile('r Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')


#Regex usando ponto de interrogação

#ocê pode pensar no ? como se dissesse “faça a correspondência de zero ou
#de uma ocorrência do grupo que antecede esse ponto de interrogação”.
#Se houver necessidade de fazer a correspondência de um caractere de ponto

phoneRegex = re.compile(r'(\d{3}-)?\d{3}-d{4}')
mo1 = phoneRegex.search('My number is 415-555-4888')
mo1.group()
print(mo1)


#Correspondente a zero ou mais ocorrências usando asterisco
#O * (chamado de asterisco) quer dizer “corresponda a zero ou mais” – o
#grupo que antecede o asterisco pode ocorrer qualquer número de vezes no
#texto. Esse grupo poderá estar totalmente ausente ou ser repetido diversas
#vezes. Vamos dar uma olhada no exemplo contendo Batman novamente.
#>>> batRegex = re.compile(r'Bat(wo)*man')
#>>> mo1 = batRegex.search('The Adventures of Batman')
#>>> mo1.group()
#'Batman'
#>>> mo2 = batRegex.search('The Adventures of Batwoman')
#>>> mo2.group()
#'Batwoman'
#>>> mo3 = batRegex.search('The Adventures of Batwowowowoman')
#>>> mo3.group()
#'Batwowowowoman'


#Correspondendo a uma ou mais ocorrências usando o sinal de
#adição
#Enquanto * quer dizer “corresponda a zero ou mais”, o + (ou sinal de adição)
#quer dizer “corresponda a um ou mais”. De modo diferente do asterisco, que
#não exige que seu grupo esteja presente na string correspondente, o grupo que
#antecede um sinal de adição deve aparecer pelo menos uma vez. Ele não é
#opcional. Digite o seguinte no shell interativo e compare o resultado com as
#regexes que usam asterisco da seção anterior:
#>>> batRegex = re.compile(r'Bat(wo)+man')
#>>> mo1 = batRegex.search('The Adventures of Batwoman')
#>>> mo1.group()
#'Batwoman'
#>>> mo2 = batRegex.search('The Adventures of Batwowowowoman')
#197>>> mo2.group()
#'Batwowowowoman'
#>>> mo3 = batRegex.search('The Adventures of Batman')
#>>> mo3 == None
#True

#Correspondências greedy e nongreedy

#As expressões regulares em Python são greedy (gulosas) por default, o que
#significa que, em situações ambíguas, a correspondência será feita com a
#maior string possível. Na versão nongreedy (não gulosa) das chaves, que faz a
#correspondência com a menor string possível, um ponto de interrogação é
#usado depois da chave de fechamento.

#Método findall()
#retorna uma lista de strings **desde que nãp haja () grupos

#criando próprias classes de caracteres


#re.DOTALL
#re.compile('.*', re.DOTALL) ignora a quebra de linha


#Correspondências sem diferenciar letras maiúsculas de minúsculas
#Para fazer sua regex ignorar as diferenças entre letras maiúsculas
#e minúsculas (ser case-insensitive), re.IGNORECASE ou re.I pode ser
#passado como segundo argumento de re.compile().

