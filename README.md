# Portuguese (Brazil) Language Pack / Pacote de Idioma Português (Brasil)

![Build](https://github.com/OtavioMiguel19/pt-br-language-pack-intellij/workflows/Build/badge.svg)
[![Version](https://img.shields.io/jetbrains/plugin/v/MARKETPLACE_ID.svg)](https://plugins.jetbrains.com/plugin/MARKETPLACE_ID)
[![Downloads](https://img.shields.io/jetbrains/plugin/d/MARKETPLACE_ID.svg)](https://plugins.jetbrains.com/plugin/MARKETPLACE_ID)

<!-- Plugin description -->
Pacote de idioma que traduz a interface dos IDEs baseados na IntelliJ Platform para **Português do Brasil (pt-BR)**.

Traduz menus, diálogos, configurações, janelas de ferramentas e outras partes da interface do usuário.

### IDEs Compatíveis
- IntelliJ IDEA
- WebStorm
- PyCharm
- PhpStorm
- GoLand
- CLion
- Rider
- RubyMine
- DataGrip
- E outros IDEs baseados na IntelliJ Platform

### Como Ativar
Após instalar o plugin, vá em **Settings → Appearance & Behavior → System Settings → Language and Region** e selecione **Português (Brasil)**.
<!-- Plugin description end -->

## Instalação

- Pelo IDE:

  <kbd>Settings/Preferences</kbd> > <kbd>Plugins</kbd> > <kbd>Marketplace</kbd> > Pesquise por **"Portuguese (Brazil) Language Pack"** > <kbd>Install</kbd>

- Manualmente:

  Baixe o [último release](https://github.com/OtavioMiguel19/pt-br-language-pack-intellij/releases/latest) e instale manualmente em
  <kbd>Settings/Preferences</kbd> > <kbd>Plugins</kbd> > <kbd>⚙️</kbd> > <kbd>Install plugin from disk...</kbd>

## Contribuindo

Contribuições são bem-vindas! Os arquivos de tradução estão em `src/main/resources/messages/`.

Cada arquivo `.properties` corresponde a um bundle de mensagens do IntelliJ Platform. As chaves devem corresponder exatamente às chaves originais dos bundles da plataforma.

## Estrutura do Projeto

```
src/main/resources/
├── META-INF/
│   └── plugin.xml                  # Configuração do plugin com languageBundle locale="pt-BR"
└── messages/
    ├── ActionsBundle.properties     # Menus e ações
    ├── AnalysisBundle.properties    # Análise de código e inspeções
    ├── ApplicationBundle.properties # Configurações do aplicativo
    ├── CodeInsightBundle.properties # Completar código, navegação
    ├── CommonBundle.properties      # Textos comuns (botões, títulos)
    ├── CopyrightBundle.properties   # Configurações de copyright
    ├── CoreBundle.properties        # Núcleo da plataforma
    ├── DatabaseBundle.properties    # Banco de dados
    ├── DebuggerBundle.properties    # Depurador
    ├── DiagnosticBundle.properties  # Erros e diagnósticos
    ├── DiffBundle.properties        # Diferenças e mesclagem
    ├── DockerBundle.properties      # Docker
    ├── EditorBundle.properties      # Editor de código
    ├── ExecutionBundle.properties   # Execução e depuração
    ├── FileTypesBundle.properties   # Tipos de arquivo
    ├── FindBundle.properties        # Busca e localização
    ├── GitBundle.properties         # Git
    ├── GradleBundle.properties      # Gradle
    ├── HttpClientBundle.properties  # Cliente HTTP
    ├── IdeBundle.properties         # Textos gerais do IDE
    ├── IndexingBundle.properties    # Indexação
    ├── JavaBundle.properties        # Java
    ├── JsonBundle.properties        # JSON
    ├── KeyMapBundle.properties      # Mapa de teclas
    ├── KotlinBundle.properties      # Kotlin
    ├── LangBundle.properties        # Funcionalidades de linguagem
    ├── MarkdownBundle.properties    # Markdown
    ├── MavenBundle.properties       # Maven
    ├── OptionsBundle.properties     # Opções e configurações
    ├── PlatformBundle.properties    # Plataforma (atualizações, licença)
    ├── ProjectBundle.properties     # Estrutura do projeto
    ├── PropertiesBundle.properties  # Arquivos de propriedades
    ├── RefactoringBundle.properties # Refatoração
    ├── RegExpBundle.properties      # Expressões regulares
    ├── ScopeBundle.properties       # Escopos
    ├── SpellCheckerBundle.properties # Verificador ortográfico
    ├── SSHBundle.properties         # SSH
    ├── TerminalBundle.properties    # Terminal
    ├── TodoBundle.properties        # TODO
    ├── ToolWindowBundle.properties  # Janelas de ferramentas
    ├── UIBundle.properties          # Componentes de UI
    ├── UsageViewBundle.properties   # Visualização de usos
    └── VcsBundle.properties         # Controle de versão
```

---
Plugin baseado no [IntelliJ Platform Plugin Template][template].

[template]: https://github.com/JetBrains/intellij-platform-plugin-template
