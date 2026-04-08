<!-- Keep a Changelog guide -> https://keepachangelog.com -->

# pt-br-language-pack-intellij Changelog

## [Unreleased]
### Added
- Implementação completa do language pack pt-BR usando `languageBundle locale="pt-BR"`
- 45 arquivos de tradução cobrindo os principais bundles da IntelliJ Platform:
  - ActionsBundle (menus, ações de arquivo, edição, busca, refatoração, execução, VCS, janela, ajuda)
  - AnalysisBundle (análise de código, inspeções, dependências, duplicatas)
  - ApplicationBundle (configurações de aparência, sistema, editor, compilação, ferramentas, tela de boas-vindas)
  - CodeInsightBundle (completar código, intenções, inspeções, navegação, documentação, dobramento)
  - CommonBundle (botões, títulos, mensagens comuns)
  - CopyrightBundle (perfis e configurações de copyright)
  - CoreBundle (botões padrão, progresso, erros)
  - DatabaseBundle (conexões, console, objetos de banco de dados)
  - DebuggerBundle (sessão, passos, pontos de interrupção, avaliação, variáveis, threads, memória)
  - DiagnosticBundle (erros, relatórios, diagnóstico de memória)
  - DiffBundle (diferenças, mesclagem, opções de comparação)
  - DockerBundle (conexões, containers, imagens, compose)
  - EditorBundle (fonte, esquema de cores, estilo de código, ações, abas, marcadores, busca)
  - ExecutionBundle (configurações de execução, depuração, pontos de interrupção, console, terminal, cobertura)
  - FileTypesBundle (tipos de arquivo conhecidos)
  - FindBundle (localizar, substituir, ir para, resultados)
  - GitBundle (branches, commit, push, pull, fetch, merge, rebase, stash, log, remoto, tag, blame, diff, status)
  - GradleBundle (configurações, tarefas, sincronização, wrapper)
  - HttpClientBundle (requisições, respostas, ambientes)
  - IdeBundle (geral, configurações, navegador, proxy, projeto, plugins, aparência, editor, VCS, notificações)
  - IndexingBundle (indexação, dumb mode, invalidar caches)
  - JavaBundle (criação, geração de código, inspeções, refatoração, compilação, execução)
  - JsonBundle (esquemas, formatação, validação)
  - KeyMapBundle (mapa de teclas, atalhos, conflitos)
  - KotlinBundle (criação, conversão, configuração, inspeções, coroutines)
  - LangBundle (estrutura de código, hierarquia, modelos dinâmicos, intenções, inspeções, completar código, navegação, refatoração)
  - MarkdownBundle (visualização, formatação, ações)
  - MavenBundle (configurações, objetivos, importação, execução)
  - OptionsBundle (categorias de configurações, aparência, editor, keymap, compilação, ferramentas, VCS)
  - PlatformBundle (atualizações, licença, sobre, feedback, dica do dia, tela de boas-vindas, notificações, histórico local, scratch)
  - ProjectBundle (estrutura do projeto, SDK, módulos, bibliotecas)
  - PropertiesBundle (chaves, valores, bundle de recursos)
  - RefactoringBundle (renomear, mover, copiar, exclusão segura, extrair, incorporar, alterar assinatura, conflitos)
  - RegExpBundle (teste, flags, correspondências)
  - ScopeBundle (escopos predefinidos e personalizados)
  - SpellCheckerBundle (verificador ortográfico, dicionários)
  - SSHBundle (conexão, autenticação, proxy, túnel)
  - TerminalBundle (sessões, configurações, cursor)
  - TodoBundle (padrões, filtros, agrupamento)
  - ToolWindowBundle (nomes das janelas de ferramentas)
  - UIBundle (seletor de arquivos, árvore, tabela, progresso, pesquisa, popup, dicas)
  - UsageViewBundle (visualização de usos, agrupamento, filtros)
  - VcsBundle (commit, branches, stash, log, diff, merge)
  - XmlBundle (XML, HTML, validação, esquemas)

### Removed
- Código de exemplo do template (MyBundle, MyProjectService, MyProjectActivity, MyToolWindowFactory)
- Arquivo messages_pt_BR.properties incorretamente posicionado na raiz de resources
- Testes de exemplo que referenciavam código removido
