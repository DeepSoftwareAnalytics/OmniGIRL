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
    'prettier/prettier':['package.json'],
    'tailwindlabs/tailwindcss':['package.json'],
    'jestjs/jest':['lerna.json','package.json'],
    'webpack/webpack':['package.json'],
    'apollographql/apollo-client':['package.json'],
    'iamkun/dayjs':['CHANGELOG.md'],
    'babel/babel':['package.json'],
    'statsmodels/statsmodels':['docs/source/release/index.rst'],
    "assertj/assertj":['pom.xml'],
    "netty/netty":['pom.xml'],
    "google/gson":['pom.xml'],
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

            'prettier/prettier',
            'tailwindlabs/tailwindcss',
            'jestjs/jest',
            'webpack/webpack',
            'babel/babel',
            'apollographql/apollo-client'
        ]
    }
)

MAP_REPO_TO_VERSION_PATTERNS.update({
    k:[
      r'<version>(\d+(\.\d+)*\.[A-Za-z][A-Za-z0-9\-]*)<\/version>', r'<version>(\d+\.\d+\.\d+(?:-\w+)?)</version>'
    ]
    for k in [
        "netty/netty",
        "assertj/assertj",
        "google/gson"
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