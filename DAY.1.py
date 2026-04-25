
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dayane Freire Soares - Educação Infantil</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        }

        header {
            background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem 0;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        nav {
            background: rgba(255,255,255,0.95);
            padding: 1rem 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }

        nav li {
            margin: 0 1.5rem;
        }

        nav a {
            text-decoration: none;
            color: #667eea;
            font-weight: bold;
            font-size: 1.1rem;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            transition: all 0.3s ease;
        }

        nav a:hover {
            background: #667eea;
            color: white;
            transform: translateY(-2px);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .section {
            background: white;
            margin: 2rem 0;
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            animation: fadeInUp 0.8s ease;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .sobre-mim {
            text-align: center;
        }

        .sobre-mim img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            margin-bottom: 1.5rem;
            border: 8px solid #ff9a9e;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }

        .sobre-mim h2 {
            color: #667eea;
            font-size: 2.2rem;
            margin-bottom: 1rem;
        }

        .formacao {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .formacao-item {
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .formacao-item:hover {
            transform: translateY(-5px);
        }

        .atividades-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .atividade {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .atividade:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }

        .atividade::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s;
        }

        .atividade:hover::before {
            left: 100%;
        }

        .atividade h3 {
            color: #667eea;
            font-size: 1.8rem;
            margin-bottom: 1rem;
        }

        .atividade button {
            background: #667eea;
            color: white;
            border: none;
            padding: 1rem 2rem;
            border-radius: 30px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 1rem;
        }

        .atividade button:hover {
            background: #764ba2;
            transform: scale(1.05);
        }

        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.8);
        }

        .modal-content {
            background: white;
            margin: 5% auto;
            padding: 2rem;
            border-radius: 20px;
            width: 90%;
            max-width: 600px;
            max-height: 80vh;
            overflow-y: auto;
            animation: modalSlideIn 0.3s ease;
        }

        @keyframes modalSlideIn {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }

        .close:hover {
            color: #667eea;
        }

        .contato {
            text-align: center;
        }

        .linkedin-btn {
            display: inline-block;
            background: #0077b5;
            color: white;
            padding: 1rem 2rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1rem;
            margin-top: 1rem;
            transition: all 0.3s ease;
        }

        .linkedin-btn:hover {
            background: #005582;
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(0,119,181,0.4);
        }

        @media (max-width: 768px) {
            header h1 {
                font-size: 2rem;
            }
            
            .container {
                padding: 1rem;
            }
            
            .section {
                padding: 1.5rem;
                margin: 1rem 0;
            }
        }

        .estrelas {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: twinkle 2s infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0; transform: scale(0); }
            50% { opacity: 1; transform: scale(1); }
        }
    </style>
</head>
<body>
    <header>
        <h1>🌟 Dayane Freire Soares 🌟</h1>
        <p>Educação Infantil com Amor e Criatividade</p>
    </header>

    <nav>
        <ul>
            <li><a href="#home">🏠 Início</a></li>
            <li><a href="#sobre">👩‍🏫 Sobre Mim</a></li>
            <li><a href="#atividades">🎮 Atividades</a></li>
            <li><a href="#contato">📞 Contato</a></li>
        </ul>
    </nav>

    <div class="container">
        <section id="home" class="section">
            <h2 style="text-align: center; color: #667eea; font-size: 2.5rem; margin-bottom: 2rem;">Bem-vindo ao Mundo Mágico da Aprendizagem! ✨</h2>
            <p style="font-size: 1.3rem; text-align: center; color: #555;">
                Aqui você encontra atividades divertidas e educativas para crianças da educação infantil. 
                Aprendizado através do brincar! 🎨📚🎵
            </p>
        </section>

        <section id="sobre" class="section sobre-mim">
            <img src="https://via.placeholder.com/200x200/667eea/ffffff?text=Dayane" alt="Dayane Freire Soares">
            <h2>Olá! Eu sou Dayane Freire Soares 👋</h2>
            <p style="font-size: 1.2rem; margin-bottom: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
                Sou pedagoga apaixonada pela educação infantil, com pós-graduação em 
                <strong>Psicopedagogia com ênfase em Educação Especial e Inclusiva</strong>. 
                Atualmente estou cursando TI para trazer ainda mais inovação para o aprendizado das crianças!
            </p>
            
            <div class="formacao">
                <div class="formacao-item">
                    <h3>🎓 Pedagogia</h3>
                    <p>Formação completa em Educação</p>
                </div>
                <div class="formacao-item">
                    <h3>🧠 Psicopedagogia</h3>
                    <p>Educação Especial e Inclusiva</p>
                </div>
                <div class="formacao-item">
                    <h3>💻 TI (cursando)</h3>
                    <p>Tecnologia na Educação</p>
                </div>
            </div>
        </section>

        <section id="atividades" class="section">
            <h2 style="text-align: center; color: #667eea; font-size: 2.5rem; margin-bottom: 2rem;">Atividades Educativas 🎉</h2>
            <div class="atividades-grid">
                <div class="atividade" onclick="openModal('numeros')">
                    <h3>🔢 Contar Números</h3>
                    <p>Aprenda a contar de 1 a 10 com animações divertidas!</p>
                    <button>Jogar Agora</button>
                </div>
                
                <div class="atividade" onclick="openModal('cores')">
                    <h3>🌈 Reconhecer Cores</h3>
                    <p>Identifique e nomeie todas as cores do arco-íris!</p>
                    <button>Jogar Agora</button>
                </div>
                
                <div class="atividade" onclick="openModal('alfabeto')">
                    <h3>🔤 Alfabeto Mágico</h3>
                    <p>Conheça as letras com sons e imagens incríveis!</p>
                    <button>Jogar Agora</button>
                </div>
                
                <div class="atividade" onclick="openModal('formas')">
                    <h3>📐 Formas Geométricas</h3>
                    <p>Descubra círculo, quadrado, triângulo e muito mais!</p>
                    <button>Jogar Agora</button>
                </div>
            </div>
        </section>

        <section id="contato" class="section contato">
            <h2 style="color: #667eea; font-size: 2.2rem; margin-bottom: 1rem;">Entre em Contato! 💌</h2>
            <p style="font-size: 1.2rem; margin-bottom: 2rem;">
                Quer mais atividades ou tem alguma sugestão? Me mande uma mensagem!
            </p>
            <a href="https://www.linkedin.com/in/dayane-freire-soares-4569235b/" target="_blank" class="linkedin-btn">
                📱 Conecte-se no LinkedIn
            </a>
        </section>
    </div>

    <!-- Modal -->
    <div id="modal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal()">&times;</span>
            <div id="modal-body">
                <!-- Conteúdo das atividades será inserido aqui -->
            </div>
        </div>
    </div>

    <script>
        function openModal(tipo) {
            const modal = document.getElementById('modal');
            const modalBody = document.getElementById('modal-body');
            
            let conteudo = '';
            
            switch(tipo) {
                case 'numeros':
                    conteudo = `
                        <h2 style="color: #667eea; text-align: center;">🔢 Jogo dos Números Mágicos</h2>
                        <div style="text-align: center; font-size: 1.5rem; margin: 2rem 0;">Aqui está um site completo e responsivo para você, Dayane! Ele inclui uma seção "Sobre Mim", atividades interativas para educação infantil e um design colorido e atrativo para crianças.

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dayane Freire Soares - Educação Infantil</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Comic Sans MS', cursive, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
        }

        header {
            background: linear-gradient(45deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem 0;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        header p {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        nav {
            background: rgba(255,255,255,0.95);
            padding: 1rem 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        nav ul {
            list-style: none;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }

        nav li {
            margin: 0 1.5rem;
        }

        nav a {
            text-decoration: none;
            color: #667eea;
            font-weight: bold;
            font-size: 1.1rem;
            padding: 0.5rem 1rem;
            border-radius: 25px;
            transition: all 0.3s ease;
        }

        nav a:hover {
            background: #667eea;
            color: white;
            transform: translateY(-2px);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .section {
            background: white;
            margin: 2rem 0;
            padding: 2.5rem;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            animation: fadeInUp 0.8s ease;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .sobre-mim {
            text-align: center;
        }

        .sobre-mim img {
            width: 200px;
            height: 200px;
            border-radius: 50%;
            margin-bottom: 1.5rem;
            border: 8px solid #ff9a9e;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }

        .sobre-mim h2 {
            color: #667eea;
            font-size: 2.2rem;
            margin-bottom: 1rem;
        }

        .formacao {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 2rem;
        }

        .formacao-item {
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 1.5rem;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }

        .formacao-item:hover {
            transform: translateY(-5px);
        }

        .atividades-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .atividade {
            background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }

        .atividade:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }

        .atividade::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
            transition: left 0.5s;
        }

        .atividade:hover::before {
            left: 100%;
        }

        .atividade h3 {
            color: #667eea;
            font-size: 1.8rem;
            margin-bottom: 1rem;
        }

        .atividade button {
            background: #667eea;
            color: white;
            border: none;
            padding: 1rem 2rem;
            border-radius: 30px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            margin-top: 1rem;
        }

        .atividade button:hover {
            background: #764ba2;
            transform: scale(1.05);
        }

        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.8);
        }

        .modal-content {
            background: white;
            margin: 5% auto;
            padding: 2rem;
            border-radius: 20px;
            width: 90%;
            max-width: 600px;
            max-height: 80vh;
            overflow-y: auto;
            animation: modalSlideIn 0.3s ease;
        }

        @keyframes modalSlideIn {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .close {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }

        .close:hover {
            color: #667eea;
        }

        .contato {
            text-align: center;
        }

        .linkedin-btn {
            display: inline-block;
            background: #0077b5;
            color: white;
            padding: 1rem 2rem;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1rem;
            margin-top: 1rem;
            transition: all 0.3s ease;
        }

        .linkedin-btn:hover {
            background: #005582;
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(0,119,181,0.4);
        }

        @media (max-width: 768px) {
            header h1 {
                font-size: 2rem;
            }
            
            .container {
                padding: 1rem;
            }
            
            .section {
                padding: 1.5rem;
                margin: 1rem 0;
            }
        }

        .estrelas {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            border-radius: 50%;
            animation: twinkle 2s infinite;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0; transform: scale(0); }
            50% { opacity: 1; transform: scale(1); }
        }
    </style>
</head>
<body>
    <header>
        <h1>🌟 Dayane Freire Soares 🌟</h1>
        <p>Educação Infantil com Amor e Criatividade</p>
    </header>

    <nav>
        <ul>
            <li><a href="#home">🏠 Início</a></li>
            <li><a href="#sobre">👩‍🏫 Sobre Mim</a></li>
            <li><a href="#atividades">🎮 Atividades</a></li>
            <li><a href="#contato">📞 Contato</a></li>
        </ul>
    </nav>

    <div class="container">
        <section id="home" class="section">
            <h2 style="text-align: center; color: #667eea; font-size: 2.5rem; margin-bottom: 2rem;">Bem-vindo ao Mundo Mágico da Aprendizagem! ✨</h2>
            <p style="font-size: 1.3rem; text-align: center; color: #555;">
                Aqui você encontra atividades divertidas e educativas para crianças da educação infantil. 
                Aprendizado através do brincar! 🎨📚🎵
            </p>
        </section>

        <section id="sobre" class="section sobre-mim">
            <img src="https://via.placeholder.com/200x200/667eea/ffffff?text=Dayane" alt="Dayane Freire Soares">
            <h2>Olá! Eu sou Dayane Freire Soares 👋</h2>
            <p style="font-size: 1.2rem; margin-bottom: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
                Sou pedagoga apaixonada pela educação infantil, com pós-graduação em 
                <strong>Psicopedagogia com ênfase em Educação Especial e Inclusiva</strong>. 
                Atualmente estou cursando TI para trazer ainda mais inovação para o aprendizado das crianças!
            </p>
            
            <div class="formacao">
                <div class="formacao-item">
                    <h3>🎓 Pedagogia</h3>
                    <p>Formação completa em Educação</p>
                </div>
                <div class="formacao-item">
                    <h3>🧠 Psicopedagogia</h3>
                    <p>Educação Especial e Inclusiva</p>
                </div>
                <div class="formacao-item">
                    <h3>💻 TI (cursando)</h3>
                    <p>Tecnologia na Educação</p>
                </div>
            </div>
        </section>

        <section id="atividades" class="section">
            <h2 style="text-align: center; color: #667eea; font-size: 2.5rem; margin-bottom: 2rem;">Atividades Educativas 🎉</h2>
            <div class="atividades-grid">
                <div class="atividade" onclick="openModal('numeros')">
                    <h3>🔢 Contar Números</h3>
                    <p>Aprenda a contar de 1 a 10 com animações divertidas!</p>
                    <button>Jogar Agora</button>
                </div>
                
                <div class="atividade" onclick="openModal('cores')">
                    <h3>🌈 Reconhecer Cores</h3>
                    <p>Identifique e nomeie todas as cores do arco-íris!</p>
                    <button>Jogar Agora</button>
                </div>
                
                <div class="atividade" onclick="openModal('alfabeto')">
                    <h3>🔤 Alfabeto Mágico</h3>
                    <p>Conheça as letras com sons e imagens incríveis!</p>
                    <button>Jogar Agora</button>
                </div>
                
                <div class="atividade" onclick="openModal('formas')">
                    <h3>📐 Formas Geométricas</h3>
                    <p>Descubra círculo, quadrado, triângulo e muito mais!</p>
                    <button>Jogar Agora</button>
                </div>
            </div>
        </section>

        <section id="contato" class="section contato">
            <h2 style="color: #667eea; font-size: 2.2rem; margin-bottom: 1rem;">Entre em Contato! 💌</h2>
            <p style="font-size: 1.2rem; margin-bottom: 2rem;">
                Quer mais atividades ou tem alguma sugestão? Me mande uma mensagem!
            </p>
            <a href="https://www.linkedin.com/in/dayane-freire-soares-4569235b/" target="_blank" class="linkedin-btn">
                📱 Conecte-se no LinkedIn
            </a>
        </section>
    </div>

    <!-- Modal -->
    <div id="modal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal()">&times;</span>
            <div id="modal-body">
                <!-- Conteúdo das atividades será inserido aqui -->
            </div>
        </div>
    </div>

    <script>
        function openModal(tipo) {
            const modal = document.getElementById('modal');
            const modalBody = document.getElementById('modal-body');
            
            let conteudo = '';
            
            switch(tipo) {
                case 'numeros':
                    conteudo = `
                        <h2 style="color: #667eea; text-align: center;">🔢 Jogo dos Números Mágicos</h2>
                        <div style="text-align: center; font-size: 1.5rem; margin: 2rem 0;">
                            <p>Conte junto comigo! 🐰</p>
                            <div id="contador" style="font-size: 4rem; margin: 2rem 0; color: #ff6b6b;">1</div>
                            <button onclick="contarNumeros()" style="background: #ff6b6b; color: white; padding: 1rem 2rem; border: none; border-radius: 25px; font-size: 1.2rem; cursor: pointer;">Próximo Número ➡️</button>
                        </div>
                        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 15px; margin-top: 2rem;">
                            <h3>🎯 Objetivo:</h3>
                            <ul style="text-align: left; font-size: 1.1rem;">
                                <li>Reconhecer números de 1 a 10</li>
                                <li>Associar quantidade com símbolo</li>
                                <li>Desenvolver coordenação motora</li>
                            </ul>
                        </div>
                    `;
                    break;
                    
                case 'cores':
                    conteudo = `
                        <h2 style="color: #667eea; text-align: center;">🌈 Caça às Cores</h2>
                        <div style="text-align: center;">
                            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin: 2rem 0;">
                                <div style="width: 80px; height: 80px; border-radius: 50%; background: #ff6b6b; cursor: pointer;" onclick="alert('VERMELHO! 🍎')" title="Clique na cor!"></div>
                                <div style="width: 80px; height: 80px; border-radius: 50%; background: #4ecdc4; cursor: pointer;" onclick="alert('AZUL! 🐳')" title="Clique na cor!"></div>
                                <div style="width: 80px; height: 80px; border-radius: 50%; background: #ffe66d; cursor: pointer;" onclick="alert('AMARELO! ☀️')" title="Clique na cor!"></div>
                            </div>
                            <p style="font-size: 1.3rem;">Clique nas cores e descubra o que elas representam!</p>
                        </div>
                    `;
                    break;
                    
                case 'alfabeto':
                    conteudo = `
                        <h2 style="color: #667eea; text-align: center;">🔤 Alfabeto Dançante</h2>
                        <div style="text-align: center; font-size: 3rem; margin: 2rem 0;">A</div>
                        <p style="font-size: 1.5rem;">🐜 Formiga, Abacaxi, Avião</p>
                        <audio controls style="margin: 2rem 0;">
                            <source src="data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJB
                            <p>Conte junto comigo! 🐰</p>
                            <div id="contador" style="font-size: 4rem; margin: 2rem 0; color: #ff6b6b;">1</div>
                            <button onclick="contarNumeros()" style="background: #ff6b6b; color: white; padding: 1rem 2rem; border: none; border-radius: 25px; font-size: 1.2rem; cursor: pointer;">Próximo Número ➡️</button>
                        </div>
                        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 15px; margin-top: 2rem;">
                            <h3>🎯 Objetivo:</h3>
                            <ul style="text-align: left; font-size: 1.1rem;">
                                <li>Reconhecer números de 1 a 10</li>
                                <li>Associar quantidade com símbolo</li>
                                <li>Desenvolver coordenação motora</li>
                            </ul>
                        </div>
                    `;
                    break;
                    
                case 'cores':
                    conteudo = `
                        <h2 style="color: #667eea; text-align: center;">🌈 Caça às Cores</h2>
                        <div style="text-align: center;">
                            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap; margin: 2rem 0;">
                                <div style="width: 80px; height: 80px; border-radius: 50%; background: #ff6b6b; cursor: pointer;" onclick="alert('VERMELHO! 🍎')" title="Clique na cor!"></div>
                                <div style="width: 80px; height: 80px; border-radius: 50%; background: #4ecdc4; cursor: pointer;" onclick="alert('AZUL! 🐳')" title="Clique na cor!"></div>
                                <div style="width: 80px; height: 80px; border-radius: 50%; background: #ffe66d; cursor: pointer;" onclick="alert('AMARELO! ☀️')" title="Clique na cor!"></div>
                            </div>
                            <p style="font-size: 1.3rem;">Clique nas cores e descubra o que elas representam!</p>
                        </div>
                    `;
                    break;
                    
                case 'alfabeto':
                    conteudo = `
                        <h2 style="color: #667eea; text-align: center;">🔤 Alfabeto Dançante</h2>
                        <div style="text-align: center; font-size: 3rem; margin: 2rem 0;">A</div>
                        <p style="font-size: 1.5rem;">🐜 Formiga, Abacaxi, Avião</p>
                        <audio controls style="margin: 2rem 0;">
                            <source src="data:audio/wav;base64,UklGRnoGAABXQVZFZm10IBAAAAABAAEAQB8AAEAfAAABAAgAZGF0YQoGAACBhYqFbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJBhNjVKMbF1fdJivrJB
