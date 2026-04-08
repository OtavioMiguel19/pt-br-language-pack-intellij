#!/usr/bin/env python3
import os, re, sys

# Phrase-level translations (applied first, longest match)
P = [
("Search Everywhere","Pesquisar em Todo Lugar"),("Find in Files","Localizar nos Arquivos"),("Find in Path","Localizar no Caminho"),("Replace in Files","Substituir nos Arquivos"),("Replace in Path","Substituir no Caminho"),("Find Usages","Localizar Usos"),("Show Usages","Mostrar Usos"),("Go to Class","Ir para Classe"),("Go to File","Ir para Arquivo"),("Go to Symbol","Ir para Simbolo"),("Go to Line","Ir para Linha"),("Go to Declaration","Ir para Declaracao"),("Go to Implementation","Ir para Implementacao"),("Go to Type Declaration","Ir para Declaracao de Tipo"),("Go to Super","Ir para Super"),("Go to Test","Ir para Teste"),("Go to Action","Ir para Acao"),("Run to Cursor","Executar ate o Cursor"),("Run/Debug","Executar/Depurar"),("Step Over","Passar Por Cima"),("Step Into","Entrar"),("Step Out","Sair"),("Force Step Over","Forcar Passagem"),("Force Step Into","Forcar Entrada"),("Evaluate Expression","Avaliar Expressao"),("Show Context Actions","Mostrar Acoes de Contexto"),("Quick Fix","Correcao Rapida"),("Quick Documentation","Documentacao Rapida"),("Quick Definition","Definicao Rapida"),("Parameter Info","Informacao de Parametro"),("Code Completion","Completar Codigo"),("Code Folding","Dobramento de Codigo"),("Code Style","Estilo de Codigo"),("Code Inspection","Inspecao de Codigo"),("Source Code","Codigo-Fonte"),("Reformat Code","Reformatar Codigo"),("Optimize Imports","Otimizar Importacoes"),("Line Comment","Comentario de Linha"),("Block Comment","Comentario de Bloco"),("Tool Window","Janela de Ferramentas"),("Tool Windows","Janelas de Ferramentas"),("Status Bar","Barra de Status"),("Navigation Bar","Barra de Navegacao"),("Editor Tabs","Abas do Editor"),("Line Numbers","Numeros de Linha"),("Soft Wraps","Quebras de Linha Automaticas"),("File Encoding","Codificacao de Arquivo"),("File Type","Tipo de Arquivo"),("File Types","Tipos de Arquivo"),("File Templates","Modelos de Arquivo"),("Live Templates","Modelos Dinamicos"),("Live Template","Modelo Dinamico"),("Color Scheme","Esquema de Cores"),("Color Schemes","Esquemas de Cores"),("Font Size","Tamanho da Fonte"),("Version Control","Controle de Versao"),("Local History","Historico Local"),("Change List","Lista de Alteracoes"),("Commit Message","Mensagem de Commit"),("Run Configuration","Configuracao de Execucao"),("Run Configurations","Configuracoes de Execucao"),("Breakpoints","Pontos de Interrupcao"),("Breakpoint","Ponto de Interrupcao"),("Stack Trace","Rastreamento de Pilha"),("Call Stack","Pilha de Chamadas"),("Project Structure","Estrutura do Projeto"),("External Tools","Ferramentas Externas"),("Power Save Mode","Modo de Economia de Energia"),("Presentation Mode","Modo de Apresentacao"),("Full Screen","Tela Cheia"),("Recent Files","Arquivos Recentes"),("Recent Locations","Locais Recentes"),("Recent Changes","Alteracoes Recentes"),("Recent Projects","Projetos Recentes"),("Tip of the Day","Dica do Dia"),("Check for Updates","Verificar Atualizacoes"),("Expand All","Expandir Tudo"),("Collapse All","Recolher Tudo"),("Select All","Selecionar Tudo"),("Show All","Mostrar Tudo"),("Hide All","Ocultar Tudo"),("Close All","Fechar Tudo"),("Remove All","Remover Tudo"),("Delete All","Excluir Tudo"),("Clear All","Limpar Tudo"),("Reset All","Redefinir Tudo"),("Sort by","Ordenar por"),("Group by","Agrupar por"),("Filter by","Filtrar por"),("Not available","Nao disponivel"),("Not found","Nao encontrado"),("Not supported","Nao suportado"),("Not specified","Nao especificado"),("No items","Nenhum item"),("No results","Nenhum resultado"),("No changes","Sem alteracoes"),("No errors","Sem erros"),("No warnings","Sem avisos"),("No problems","Sem problemas"),("No usages","Nenhum uso"),("Nothing found","Nada encontrado"),("Nothing here","Nada aqui"),("Please wait","Por favor, aguarde"),("Cannot create","Nao e possivel criar"),("Cannot open","Nao e possivel abrir"),("Cannot find","Nao e possivel encontrar"),("Cannot delete","Nao e possivel excluir"),("Cannot rename","Nao e possivel renomear"),("Cannot move","Nao e possivel mover"),("Cannot copy","Nao e possivel copiar"),("Cannot save","Nao e possivel salvar"),("Cannot read","Nao e possivel ler"),("Cannot write","Nao e possivel gravar"),("Cannot load","Nao e possivel carregar"),("Cannot connect","Nao e possivel conectar"),("Cannot run","Nao e possivel executar"),("Cannot start","Nao e possivel iniciar"),("Unable to","Nao e possivel"),("Failed to","Falha ao"),("Do you want to","Deseja"),("Are you sure","Tem certeza"),("already exists","ja existe"),("does not exist","nao existe"),("has been","foi"),("will be","sera"),("could not","nao foi possivel"),("Could not","Nao foi possivel"),("Click to","Clique para"),("Right-click","Clique com botao direito"),("Double-click","Clique duplo"),("Read-only","Somente leitura"),("Read Only","Somente Leitura"),("Out of memory","Memoria insuficiente"),("in progress","em andamento"),("at caret","no cursor"),("from clipboard","da area de transferencia"),("to clipboard","para a area de transferencia"),("from scratch","do zero"),("Split Vertically","Dividir Verticalmente"),("Split Horizontally","Dividir Horizontalmente"),
]

# Word-level translations
W = {
"File":"Arquivo","Edit":"Editar","View":"Exibir","Navigate":"Navegar","Code":"Codigo","Refactor":"Refatorar","Build":"Compilar","Run":"Executar","Tools":"Ferramentas","Window":"Janela","Help":"Ajuda","Settings":"Configuracoes","Preferences":"Preferencias","Project":"Projeto","Module":"Modulo","Library":"Biblioteca","Libraries":"Bibliotecas","Plugin":"Plugin","Plugins":"Plugins","Template":"Modelo","Templates":"Modelos","Scheme":"Esquema","Profile":"Perfil","Scope":"Escopo","Action":"Acao","Actions":"Acoes","Shortcut":"Atalho","Shortcuts":"Atalhos",
"Open":"Abrir","Close":"Fechar","Save":"Salvar","Delete":"Excluir","Remove":"Remover","Add":"Adicionar","Create":"Criar","New":"Novo","Copy":"Copiar","Cut":"Recortar","Paste":"Colar","Move":"Mover","Rename":"Renomear","Find":"Localizar","Replace":"Substituir","Search":"Pesquisar","Filter":"Filtrar","Sort":"Ordenar","Refresh":"Atualizar","Reload":"Recarregar","Restart":"Reiniciar","Reset":"Redefinir","Restore":"Restaurar","Revert":"Reverter","Undo":"Desfazer","Redo":"Refazer","Apply":"Aplicar","Cancel":"Cancelar","OK":"OK","Yes":"Sim","No":"Nao","Accept":"Aceitar","Decline":"Recusar","Submit":"Enviar","Continue":"Continuar","Skip":"Pular","Retry":"Tentar Novamente","Abort":"Abortar","Stop":"Parar","Pause":"Pausar","Resume":"Retomar",
"Enable":"Habilitar","Disable":"Desabilitar","Enabled":"Habilitado","Disabled":"Desabilitado","Show":"Mostrar","Hide":"Ocultar","Expand":"Expandir","Collapse":"Recolher","Toggle":"Alternar","Select":"Selecionar","Selected":"Selecionado","Selection":"Selecao","Deselect":"Desselecionar","Check":"Marcar","Uncheck":"Desmarcar","Include":"Incluir","Exclude":"Excluir","Import":"Importar","Export":"Exportar","Upload":"Enviar","Download":"Baixar","Install":"Instalar","Uninstall":"Desinstalar","Update":"Atualizar","Upgrade":"Atualizar",
"Start":"Iniciar","Finish":"Concluir","Begin":"Iniciar","End":"Fim","Next":"Proximo","Previous":"Anterior","Back":"Voltar","Forward":"Avancar","Up":"Acima","Down":"Abaixo","Left":"Esquerda","Right":"Direita","Top":"Topo","Bottom":"Final","First":"Primeiro","Last":"Ultimo","Before":"Antes","After":"Depois","Above":"Acima","Below":"Abaixo",
"Error":"Erro","Errors":"Erros","Warning":"Aviso","Warnings":"Avisos","Information":"Informacao","Info":"Info","Hint":"Dica","Hints":"Dicas","Note":"Nota","Message":"Mensagem","Messages":"Mensagens","Notification":"Notificacao","Notifications":"Notificacoes","Problem":"Problema","Problems":"Problemas","Issue":"Problema","Issues":"Problemas","Bug":"Bug","Suggestion":"Sugestao","Suggestions":"Sugestoes",
"Name":"Nome","Type":"Tipo","Value":"Valor","Description":"Descricao","Details":"Detalhes","Summary":"Resumo","Title":"Titulo","Label":"Rotulo","Text":"Texto","Content":"Conteudo","Path":"Caminho","Location":"Localizacao","Directory":"Diretorio","Folder":"Pasta","Package":"Pacote","Class":"Classe","Interface":"Interface","Method":"Metodo","Function":"Funcao","Variable":"Variavel","Constant":"Constante","Field":"Campo","Property":"Propriedade","Parameter":"Parametro","Argument":"Argumento","Return":"Retorno","Result":"Resultado","Output":"Saida","Input":"Entrada",
"Editor":"Editor","Console":"Console","Terminal":"Terminal","Browser":"Navegador","Server":"Servidor","Client":"Cliente","Database":"Banco de Dados","Table":"Tabela","Column":"Coluna","Row":"Linha","Index":"Indice","Schema":"Esquema","Query":"Consulta",
"Commit":"Confirmar","Push":"Enviar","Pull":"Puxar","Fetch":"Buscar","Merge":"Mesclar","Rebase":"Rebase","Branch":"Branch","Branches":"Branches","Tag":"Tag","Tags":"Tags","Stash":"Stash","Clone":"Clonar","Checkout":"Checkout","Diff":"Diferencas","Blame":"Blame","Log":"Log","History":"Historico","Annotate":"Anotar","Revert":"Reverter",
"Debug":"Depurar","Debugger":"Depurador","Debugging":"Depuracao","Execute":"Executar","Execution":"Execucao","Running":"Executando","Compile":"Compilar","Compiler":"Compilador","Compilation":"Compilacao","Test":"Teste","Tests":"Testes","Testing":"Testando","Coverage":"Cobertura","Inspect":"Inspecionar","Inspection":"Inspecao","Inspections":"Inspecoes","Analysis":"Analise","Analyze":"Analisar",
"Appearance":"Aparencia","Behavior":"Comportamento","General":"Geral","Advanced":"Avancado","Basic":"Basico","Custom":"Personalizado","Default":"Padrao","Standard":"Padrao","Optional":"Opcional","Required":"Obrigatorio","Automatic":"Automatico","Manual":"Manual",
"Loading":"Carregando","Saving":"Salvando","Processing":"Processando","Searching":"Pesquisando","Indexing":"Indexando","Scanning":"Verificando","Updating":"Atualizando","Downloading":"Baixando","Uploading":"Enviando","Installing":"Instalando","Configuring":"Configurando","Initializing":"Inicializando","Connecting":"Conectando","Disconnecting":"Desconectando","Synchronizing":"Sincronizando","Resolving":"Resolvendo","Analyzing":"Analisando","Compiling":"Compilando","Building":"Compilando","Deploying":"Implantando","Formatting":"Formatando","Generating":"Gerando","Collecting":"Coletando","Calculating":"Calculando","Validating":"Validando","Preparing":"Preparando","Cleaning":"Limpando","Deleting":"Excluindo","Copying":"Copiando","Moving":"Movendo","Renaming":"Renomeando",
"Color":"Cor","Colors":"Cores","Font":"Fonte","Fonts":"Fontes","Size":"Tamanho","Width":"Largura","Height":"Altura","Margin":"Margem","Padding":"Preenchimento","Border":"Borda","Background":"Fundo","Foreground":"Primeiro Plano","Bold":"Negrito","Italic":"Italico","Underline":"Sublinhado","Strikethrough":"Tachado",
"Syntax":"Sintaxe","Semantic":"Semantico","Lexical":"Lexico","Grammar":"Gramatica","Spelling":"Ortografia","Completion":"Completar","Suggestion":"Sugestao","Annotation":"Anotacao","Annotations":"Anotacoes","Declaration":"Declaracao","Definition":"Definicao","Reference":"Referencia","References":"Referencias","Usage":"Uso","Usages":"Usos","Occurrence":"Ocorrencia","Occurrences":"Ocorrencias","Symbol":"Simbolo","Symbols":"Simbolos","Identifier":"Identificador","Keyword":"Palavra-chave","Keywords":"Palavras-chave","Literal":"Literal","Comment":"Comentario","Comments":"Comentarios","String":"String","Number":"Numero","Boolean":"Booleano","Array":"Array","Object":"Objeto","Null":"Nulo",
"Configuration":"Configuracao","Configurations":"Configuracoes","Option":"Opcao","Options":"Opcoes","Preference":"Preferencia","Feature":"Funcionalidade","Features":"Funcionalidades","Capability":"Capacidade","Permission":"Permissao","Permissions":"Permissoes","Access":"Acesso","Security":"Seguranca","Authentication":"Autenticacao","Authorization":"Autorizacao","Credential":"Credencial","Credentials":"Credenciais","Password":"Senha","Username":"Nome de usuario","Token":"Token","Certificate":"Certificado",
"Connection":"Conexao","Connections":"Conexoes","Remote":"Remoto","Local":"Local","Host":"Host","Port":"Porta","Protocol":"Protocolo","Proxy":"Proxy","Timeout":"Tempo limite","Retry":"Tentar novamente","Retries":"Tentativas",
"Success":"Sucesso","Failure":"Falha","Complete":"Completo","Completed":"Concluido","Incomplete":"Incompleto","Pending":"Pendente","Active":"Ativo","Inactive":"Inativo","Available":"Disponivel","Unavailable":"Indisponivel","Valid":"Valido","Invalid":"Invalido","Empty":"Vazio","Full":"Cheio","Existing":"Existente","Missing":"Ausente","Unknown":"Desconhecido","Undefined":"Indefinido","Deprecated":"Obsoleto","Experimental":"Experimental","Internal":"Interno","External":"Externo","Public":"Publico","Private":"Privado","Protected":"Protegido","Static":"Estatico","Abstract":"Abstrato","Final":"Final","Virtual":"Virtual","Override":"Sobrescrever","Implement":"Implementar",
"Today":"Hoje","Yesterday":"Ontem","Tomorrow":"Amanha","Now":"Agora","Never":"Nunca","Always":"Sempre","Sometimes":"As vezes","Once":"Uma vez","Twice":"Duas vezes","All":"Tudo","None":"Nenhum","Some":"Alguns","Any":"Qualquer","Every":"Cada","Each":"Cada","Other":"Outro","Another":"Outro","Same":"Mesmo","Different":"Diferente","Similar":"Similar","New":"Novo","Old":"Antigo","Current":"Atual","Latest":"Mais recente","Newest":"Mais novo","Oldest":"Mais antigo",
"and":"e","or":"ou","but":"mas","not":"nao","with":"com","without":"sem","for":"para","from":"de","into":"em","about":"sobre","between":"entre","through":"atraves","during":"durante","before":"antes","after":"depois","above":"acima","below":"abaixo","under":"sob","over":"sobre",
"the":"o","a":"um","an":"um","this":"este","that":"aquele","these":"estes","those":"aqueles","is":"e","are":"sao","was":"foi","were":"foram","been":"sido","being":"sendo","have":"ter","has":"tem","had":"tinha","having":"tendo","do":"fazer","does":"faz","did":"fez","doing":"fazendo","will":"vai","would":"iria","shall":"deve","should":"deveria","may":"pode","might":"poderia","can":"pode","must":"deve",
"Workspace":"Espaco de Trabalho","workspace":"espaco de trabalho","Bookmark":"Marcador","Bookmarks":"Marcadores","Favorite":"Favorito","Favorites":"Favoritos","Scratch":"Scratch","Scratches":"Scratches","Snippet":"Trecho","Snippets":"Trechos","Fragment":"Fragmento","Fragments":"Fragmentos","Chunk":"Bloco","Region":"Regiao","Section":"Secao","Segment":"Segmento","Block":"Bloco","Blocks":"Blocos","Group":"Grupo","Groups":"Grupos","Category":"Categoria","Categories":"Categorias","Item":"Item","Items":"Itens","Element":"Elemento","Elements":"Elementos","Entry":"Entrada","Entries":"Entradas","Record":"Registro","Records":"Registros",
}

def translate_value(val):
    if not val or not val.strip():
        return val
    # Skip values that are just placeholders, numbers, or technical
    if re.match(r'^[\s{}\d.,;:/<>()\\|&@#$%^*+=\-\[\]!?\'"~`]+$', val):
        return val
    if val.startswith('<') or val.startswith('http') or val.startswith('com.'):
        return val
    # Apply phrase translations first
    result = val
    for en, pt in P:
        result = result.replace(en, pt)
    # Apply word translations with word boundaries
    for en, pt in W.items():
        # Only replace whole words, preserve case patterns
        result = re.sub(r'\b' + re.escape(en) + r'\b', pt, result)
    return result

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    out = []
    continuation = False
    for line in lines:
        stripped = line.rstrip('\n\r')
        # Comments and blank lines: keep as-is
        if not stripped or stripped.startswith('#') or stripped.startswith('!'):
            out.append(stripped)
            continuation = False
            continue
        # Continuation lines
        if continuation:
            if stripped.endswith('\\'):
                out.append(translate_value(stripped[:-1]) + '\\')
                continuation = True
            else:
                out.append(translate_value(stripped))
                continuation = False
            continue
        # Key=value lines
        m = re.match(r'^([^=:]+?)\s*[=:]\s*(.*)', stripped)
        if m:
            key = m.group(1)
            val = m.group(2)
            if val.endswith('\\'):
                translated = translate_value(val[:-1]) + '\\'
                continuation = True
            else:
                translated = translate_value(val)
                continuation = False
            out.append(f'{key}={translated}')
        else:
            out.append(stripped)
            continuation = False
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')

def main():
    msg_dir = os.path.join(os.path.dirname(__file__), 'src', 'main', 'resources', 'messages')
    if not os.path.isdir(msg_dir):
        print(f"Directory not found: {msg_dir}")
        sys.exit(1)
    
    count = 0
    for fname in sorted(os.listdir(msg_dir)):
        if fname.endswith('.properties'):
            fpath = os.path.join(msg_dir, fname)
            process_file(fpath)
            count += 1
            print(f"Translated: {fname}")
    print(f"\nDone! Translated {count} files.")

if __name__ == '__main__':
    main()
