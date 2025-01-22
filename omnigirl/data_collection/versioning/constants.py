# Constants - Task Instance Version File
MAP_REPO_TO_VERSION_PATHS = {
    "dbt-labs/dbt-core": ["core/dbt/version.py", "core/dbt/__init__.py"],
    "django/django": ["django/__init__.py"],
    "huggingface/transformers": ["src/transformers/__init__.py"],
    "marshmallow-code/marshmallow": ["src/marshmallow/__init__.py"],
    "mwaskom/seaborn": ["seaborn/__init__.py"],
    "pallets/flask": ["src/flask/__init__.py", "flask/__init__.py"],
    "psf/requests": ["requests/__version__.py", "requests/__init__.py"],
    "pyca/cryptography": [
        "src/cryptography/__about__.py",
        "src/cryptography/__init__.py",
    ],
    "pylint-dev/astroid": ["astroid/__pkginfo__.py", "astroid/__init__.py"],
    "pylint-dev/pylint": ["pylint/__pkginfo__.py", "pylint/__init__.py"],
    "pytest-dev/pytest": ["src/_pytest/_version.py", "_pytest/_version.py"],
    "pyvista/pyvista": ["pyvista/_version.py", "pyvista/__init__.py"],
    "Qiskit/qiskit": ["qiskit/VERSION.txt"],
    "scikit-learn/scikit-learn": ["sklearn/__init__.py"],
    "sphinx-doc/sphinx": ["sphinx/__init__.py"],
    "sympy/sympy": ["sympy/release.py", "sympy/__init__.py"],
    "pillow/pillow":["src/PIL/_version.py"],
    'dateutil/dateutil': ['NEWS'],
    'python/mypy': ['mypy/version.py'],
    'redis/redis-py': ['setup.py','redis/__init__.py'],
    'tqdm/tqdm': ['tqdm/_version.py'],
    'urllib3/urllib3':['src/urllib3/_version.py','src/urllib3/__init__.py','urllib3/__init__.py'],
    'microsoft/TypeScript':['package.json'],
    'vercel/next.js':['package.json'],
    'facebook/react':['package.json'],

    'prettier/prettier':['package.json'],
    'eslint/eslint':['package.json'],
    'Automattic/mongoose':['package.json'],
    'tailwindlabs/tailwindcss':['package.json'],
    'vitejs/vite':['package.json'],
    'jestjs/jest':['lerna.json','package.json'],
    'nodejs/undici':['package.json'],
    'markedjs/marked':['package.json'],
    'date-fns/date-fns':['package.json'],
    'webpack/webpack':['package.json'],
    'iamkun/dayjs':['CHANGELOG.md'],
    'mochajs/mocha':['package.json'],
    'babel/babel':['package.json'],
    'statsmodels/statsmodels':['docs/source/release/index.rst'],
    'jetty/jetty.project':['pom.xml'],
    "h2database/h2database":['h2/pom.xml'],
    "assertj/assertj":['pom.xml'],
    "netty/netty":['pom.xml'],
    "projectlombok/lombok":['doc/maven-pom.xml'],#动态插入
    "google/gson":['pom.xml'],
    "junit-team/junit5":['gradle.properties'],
    "ReactiveX/RxJava":['gradle.properties'],
    "testng-team/testng":['gradle.properties'],
    "apache/groovy":['gradle.properties'],
    "square/retrofit":['gradle.properties'],
    "spockframework/spock":['build.gradle'],
    "square/okhttp":['build.gradle.kts']
}

# Cosntants - Task Instance Version Regex Pattern
MAP_REPO_TO_VERSION_PATTERNS = {
    k: [r'__version__ = [\'"](.*)[\'"]', r"VERSION = \((.*)\)"]
    
    for k in [
        "dbt-labs/dbt-core",
        "django/django",
        "huggingface/transformers",
        "marshmallow-code/marshmallow",
        "mwaskom/seaborn",
        "pallets/flask",
        "psf/requests",
        "pyca/cryptography",
        "pylint-dev/astroid",
        "pylint-dev/pylint",
        "scikit-learn/scikit-learn",
        "sphinx-doc/sphinx",
        "sympy/sympy",
        'python/mypy',
        'urllib3/urllib3',
    ]
}
MAP_REPO_TO_VERSION_PATTERNS.update({
    k: [
        r'\[\s*(\d+\.\d+\.\d+)\s*\]'
        ] for k in ['iamkun/dayjs']
})
MAP_REPO_TO_VERSION_PATTERNS.update({
    k: [
        r'version(\d+\.\d+(?:\.\d+)?(?:-\d+)?)'
        ] for k in ['statsmodels/statsmodels']
})
MAP_REPO_TO_VERSION_PATTERNS.update(
    {
        k: [
            r'"version":\s*"([^"]+)"'
            
        ]
        for k in [
            'microsoft/TypeScript',
                    
            'vercel/next.js',
            'facebook/react',

            'prettier/prettier',
            'eslint/eslint',
            'Automattic/mongoose',
            'tailwindlabs/tailwindcss',
            'vitejs/vite',
            'jestjs/jest',
            'nodejs/undici',
            'markedjs/marked',
            'date-fns/date-fns',
            'webpack/webpack',
            'mochajs/mocha',
            'babel/babel'
        ]
    }
)

MAP_REPO_TO_VERSION_PATTERNS.update({
    k:[
      r'<version>(\d+(\.\d+)*\.[A-Za-z][A-Za-z0-9\-]*)<\/version>', r'<version>(\d+\.\d+\.\d+(?:-\w+)?)</version>'
    ]
    for k in [
        "netty/netty",
        "jetty/jetty.project",
        "h2database/h2database",
        "projectlombok/lombok",
        "assertj/assertj",
        "google/gson"
        ]}
)

MAP_REPO_TO_VERSION_PATTERNS.update({
    k:[
      r'(?<=testng\.version=)(\d+(\.\d+)*)'
    ]
    for k in [
            "testng-team/testng"     
        ]}
)

MAP_REPO_TO_VERSION_PATTERNS.update({
    k:[
      r'(?:release\.version|version)\s*=\s*(\d+(\.\d+)*(-[A-Za-z0-9]+)*)'
    ]
    for k in [
            "junit-team/junit5",  
            "ReactiveX/RxJava"   
        ]}
)

MAP_REPO_TO_VERSION_PATTERNS.update({
    k:[
      r'(?<=groovyVersion=)(\d+(\.\d+)*(-[A-Za-z0-9]+)*)'
    ]
    for k in [
            "apache/groovy"    
        ]}
)


MAP_REPO_TO_VERSION_PATTERNS.update({
    k:[
      r'VERSION_NAME\s*=\s*(\d+(\.\d+)*(-[A-Za-z0-9]+)*)'
    ]
    for k in [
            "square/retrofit"      
        ]}
)

MAP_REPO_TO_VERSION_PATTERNS.update(
    {
        k: [
            r'__version__ = [\'"](.*)[\'"]',
            r'__version__ = version = [\'"](.*)[\'"]',
            r"VERSION = \((.*)\)",
        ]
        for k in ["pytest-dev/pytest", "matplotlib/matplotlib"]
    }
)
MAP_REPO_TO_VERSION_PATTERNS.update({k: [r"Version\s+(\d+\.\d+(?:\.\d+)?)"] for k in ["dateutil/dateutil"]})
MAP_REPO_TO_VERSION_PATTERNS.update({k: [r"(.*)"] for k in ["Qiskit/qiskit"]})
MAP_REPO_TO_VERSION_PATTERNS.update({k: [r"version_info = [\d]+,[\d\s]+,"] for k in ["pyvista/pyvista"]})
MAP_REPO_TO_VERSION_PATTERNS.update({k:[r"version_info = [\d]+, [\d]+, [\d\s]+"] for k in ['tqdm/tqdm']})
MAP_REPO_TO_VERSION_PATTERNS.update(
    {
        k: [
            
           r'version="(.*?)"',
           r'__version__ = [\'"](.*)[\'"]',

        ]
        for k in ['redis/redis-py']
    }
)
SWE_BENCH_URL_RAW = 'https://github.com/'
# SWE_BENCH_URL_RAW = "https://raw.githubusercontent.com/"