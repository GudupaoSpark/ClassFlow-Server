"""
常量存储
"""

import os
import uuid
import hashlib
from encrypt.dh import DH
import hashlib

VERSIONTAG = (1, 0, 0)
VERSION = '.'.join(str(i) for i in VERSIONTAG)
INDEX="""<html>

<head>
    <title>ClassFlow | 服务器</title>
    <style>
        :root {
            --primary: #2563eb;
            --text: #1f2937;
            --bg: #f8fafc;
            --container-bg: white;
            --base-url-bg: #e0e7ff;
            --warning-bg: #fee2e2;
            --warning-text: #991b1b;
            --notice-bg: #fef3c7;
            --notice-text: #92400e;
        }

        @media (prefers-color-scheme: dark) {
            :root {
                --primary: #3b82f6;
                --text: #f3f4f6;
                --bg: #111827;
                --container-bg: #1f2937;
                --base-url-bg: #1e3a8a;
                --warning-bg: #7f1d1d;
                --warning-text: #fecaca;
                --notice-bg: #78350f;
                --notice-text: #fef3c7;
            }
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            color: var(--text);
            background: var(--bg);
            margin: 0;
            padding: 2rem;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
            background: var(--container-bg);
            border-radius: 1rem;
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        }

        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 2rem;
            color: var(--primary);
            display: flex;
            align-items: center;
            gap: 2rem;
        }

        .logo-text {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .logo-text div:first-child {
            font-size: 2.5rem;
        }

        .logo-text div:last-child {
            font-size: 1.5rem;
        }

        .shield-icon {
            fill: var(--primary);
        }

        nav a {
            display: inline-block;
            padding: 0.75rem 1.5rem;
            color: white;
            background: var(--primary);
            text-decoration: none;
            border-radius: 0.5rem;
            font-weight: 500;
            transition: all 0.2s;
            margin-right: 1rem;
        }

        nav a:hover {
            background: #1d4ed8;
            transform: translateY(-1px);
        }


        .base-url {
            font-weight: bold;
            color: var(--primary);
            background: var(--base-url-bg);
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
        }

        .your-url {
            margin: 2rem 0;
            padding: 1rem;
            background: var(--container-bg);
            border: 2px solid var(--primary);
            border-radius: 0.5rem;
            font-size: 1.1rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .copy-button {
            padding: 0.5rem 1rem;
            background: var(--primary);
            color: white;
            border: none;
            border-radius: 0.25rem;
            cursor: pointer;
            transition: all 0.2s;
        }

        .copy-button:hover {
            background: #1d4ed8;
        }

        .copy-button.copied {
            background: #059669;
        }

        .warning,
        .notice {
            margin-top: 2rem;
            padding: 1rem;
            border-radius: 0.5rem;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .warning {
            background: var(--warning-bg);
            color: var(--warning-text);
        }

        .notice {
            background: linear-gradient(45deg, #8b5e34, #d97706, #b45309);
            /* 增加渐变色层次 */
            color: #fef3c7;
            /* 浅黄色文字，提供柔和对比 */
            margin-top: 0;
            margin-bottom: 2rem;
            font-size: 1.2rem;
            font-weight: bold;
            padding: 1.5rem;
            border: 3px solid currentColor;
            animation: pulse 1s infinite;
        }


        @keyframes pulse {
            0% {
                box-shadow: 0 0 0 0 rgba(146, 64, 14, 0.4);
            }

            70% {
                box-shadow: 0 0 0 10px rgba(146, 64, 14, 0);
            }

            100% {
                box-shadow: 0 0 0 0 rgba(146, 64, 14, 0);
            }
        }

        .warning-icon {
            width: 24px;
            height: 24px;
            flex-shrink: 0;
        }

        @media (prefers-color-scheme: dark) {
            .notice {
                animation: pulse-dark 1s infinite;
            }

            @keyframes pulse-dark {
                0% {
                    box-shadow: 0 0 0 0 rgba(254, 243, 199, 0.4);
                }

                70% {
                    box-shadow: 0 0 0 10px rgba(254, 243, 199, 0);
                }

                100% {
                    box-shadow: 0 0 0 0 rgba(254, 243, 199, 0);
                }
            }
        }

        .version {
            margin: 1.5rem 0;
            font-size: 1.3rem;
            color: var(--text);
            /* 常规文字颜色 */
        }

        .license {
            font-size: 0.9rem;
            text-align: center;
            color: var(--text);
            padding: 1rem;
            margin-top: 2rem;
            background: var(--container-bg);
            border-top: 1px solid rgba(0, 0, 0, 0.1);
            border-radius: 0 0 1rem 1rem;
        }

        .license a {
            color: var(--primary);
            text-decoration: none;
            font-weight: bold;
        }

        .license a:hover {
            text-decoration: underline;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="logo">
            <img alt="SafeSpeak shield logo icon" src="/favicon.ico" width="128" height="128" />
            <div class="logo-text">
                <div>ClassFlow | 服务器</div>
                <div>更好的同步课表</div>
            </div>
        </div>


        <div class="your-url">
            <div>该服务器的 URL 为：<span class="base-url">BASE_URL</span></div>
            <button class="copy-button" onclick="copyUrl()">复制</button>
        </div>
        
        <div class="version">
            服务器版本：<span class="base-url">VERSION</span>
        </div>

        <nav>
            <a href="https://class.gudupao.top">查看官方文档</a>
            <a href="/docs">查看 API 文档</a>
            <a href="https://github.com/GudupaoSpark/ClassFlow">项目仓库</a>
        </nav>
        <div class="warning">
            <svg class="warning-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
                <path fill-rule="evenodd"
                    d="M9.401 3.003c1.155-2 4.043-2 5.197 0l7.355 12.748c1.154 2-.29 4.5-2.599 4.5H4.645c-2.309 0-3.752-2.5-2.598-4.5L9.4 3.003zM12 8.25a.75.75 0 01.75.75v3.75a.75.75 0 01-1.5 0V9a.75.75 0 01.75-.75zm0 8.25a.75.75 0 100-1.5.75.75 0 000 1.5z"
                    clip-rule="evenodd" />
            </svg>
            本服务器为第三方部署，与 Gudupao 无关。
        </div>
        <div class="license">
            本项目遵循 <a href="https://github.com/GudupaoSpark/ClassFlow-Server/blob/main/LICENSE" target="_blank">MIT License</a> 许可协议。
            <br>Copyright © 2024 Gudupao.
        </div>
    </div>

    <script>
        function copyUrl() {
            const url = "BASE_URL";
            navigator.clipboard.writeText(url).then(() => {
                const button = document.querySelector('.copy-button');
                button.textContent = '已复制';
                button.classList.add('copied');
                setTimeout(() => {
                    button.textContent = '复制';
                    button.classList.remove('copied');
                }, 2000);
            });
        }
    </script>

</body>

</html>""".replace("VERSION", VERSION)



# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

computer_id = hashlib.sha256(str(uuid.getnode()).encode()).hexdigest()

dh = DH()
print(f"DH公钥：{hashlib.sha256(dh.get_public_key()).hexdigest()}")