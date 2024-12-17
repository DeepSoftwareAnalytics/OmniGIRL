import json
from tabulate import tabulate
import argparse
import datetime
def analyze_data(mode,input_dir):
    with open('benchmark/OmniGIRL.json','r')as f:
        benchmark = json.load(f)



    instance_id_list = [data['instance_id'] for data in benchmark]
    # input_dir = 'agentless.eval_qwen_agentlessX.json'
    # input_dir = 'Qwen2.5-72B-Instruct-128K.eval_claude_oracle_retrieval.json'
    with open(input_dir,'r')as f:
        results = json.load(f)
    resolved_idx_list = results['resolved_ids']
    applied_idx_list = results['completed_ids']
    # repo_list = ['webpack','tailwindcss','jest','prettier','babel','dayjs','tqdm','statsmodels','redis-py','cryptography','mypy','dateutil','netty','gson','assertj']
    if mode == 'repository':
        repo_idx_dict={}
        repo_resolved_idx_dict={}
        repo_applied_idx_dict={}
        for instance_id in instance_id_list:
            repo = instance_id.split('-')[0].replace('__','/').strip()
            repo = repo.replace('/redis','/redis-py')
            repo_idx_dict.setdefault(repo, []).append(instance_id)

        for instance_id in resolved_idx_list:
            repo = instance_id.split('-')[0].replace('__','/').strip()
            repo = repo.replace('/redis','/redis-py')
            repo_resolved_idx_dict.setdefault(repo, []).append(instance_id)

        for instance_id in applied_idx_list:
            repo = instance_id.split('-')[0].replace('__','/').strip()
            repo = repo.replace('/redis','/redis-py')
            repo_applied_idx_dict.setdefault(repo, []).append(instance_id)

        # print(repo_resolved_idx_dict)

        data = []
        for repo_name,v in repo_idx_dict.items():
            repo_data = []
            # print(repo_name)
            # input()
            repo_data.append(repo_name)
            total_num = len(v)
            resolved_num=len(repo_resolved_idx_dict.get(repo_name,[]))
            # print(resolved_num)
            # input()
            applied_num=len(repo_applied_idx_dict.get(repo_name,[]))
            repo_data.append(total_num)
            repo_data.append(resolved_num)
            repo_data.append(applied_num)

            data.append(repo_data)
        pl_repo_dict={
            'webpack':'JavaScript',
            'tailwindcss':'TypeScript',
            'jest':'TypeScript',
            'prettier':'JavaScript',
            'babel':'TypeScript',
            'dayjs':'JavaScript',
            'tqdm':'Python',
            'statsmodels':'Python',
            'redis-py':'Python',
            'cryptography':'Python',
            'mypy':'Python',
            'dateutil':'Python',
            'netty':'Java',
            'gson':'Java',
            'assertj':'Java'
        }
        pl_data_dict={
            'JavaScript':['JavaScript',0,0,0],
            'TypeScript':['TypeScript',0,0,0],
            'Java':['Java',0,0,0],
            'Python':['Python',0,0,0],

        }
        for d in data:
            # print(d)
            # input()
            pl= pl_repo_dict[d[0].split('/')[1].strip()]
            for idx in range(1,len(d)):
                # print(idx)
                # input()
                pl_data_dict[pl][idx] += d[idx]
        for k,v in pl_data_dict.items():
            data.append(v)

            
        total_data = ['Total',len(instance_id_list),len(resolved_idx_list),len(applied_idx_list)]
        data.append(total_data)
        for d in data:
            d.append(d[2]/d[1])
            d.append(d[3]/d[1])

        # 定义表头
        headers = ["Repository", "Total Instance Numbers", "Resolved Instance Numbers","Applied Instance Numbers","Resolve Rate","Applied Rate"]


        print("\nResult Analysis:")
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    elif mode == 'year':
        year_idx_dict = {}
        year_resolved_idx_dict = {}
        year_applied_idx_dict = {}

        # Create a mapping from instance_id to year
        instance_id_to_year = {}
        
        for data in benchmark:
            instance_id = data['instance_id']
            year = data['created_at'].split('-')[0]
            if int(year) <= 2017:
                year = '2017 Before '
            instance_id_to_year[instance_id] = year
            year_idx_dict.setdefault(year, []).append(instance_id)

        # Use the mapping to get years for resolved and applied instance IDs
        for instance_id in resolved_idx_list:
            instance_id = instance_id.split('_version')[0]
            year = instance_id_to_year.get(instance_id)
            if year:
                year_resolved_idx_dict.setdefault(year, []).append(instance_id)

        for instance_id in applied_idx_list:
            instance_id = instance_id.split('_version')[0]
            year = instance_id_to_year.get(instance_id)
            if year:
                year_applied_idx_dict.setdefault(year, []).append(instance_id)

        data = []
        for year, v in year_idx_dict.items():
            total_instances = len(v)
            resolved_instances = len(year_resolved_idx_dict.get(year, []))
            applied_instances = len(year_applied_idx_dict.get(year, []))
            resolve_rate = resolved_instances / total_instances if total_instances > 0 else 0
            applied_rate = applied_instances / total_instances if total_instances > 0 else 0
            data.append([year, total_instances, resolved_instances, applied_instances, resolve_rate, applied_rate])

        headers = ["Year", "Total Instance Numbers", "Resolved Instance Numbers", "Applied Instance Numbers", "Resolve Rate", "Applied Rate"]

        # Print the table
        print("\nResult Analysis:")
        print(tabulate(sorted(data, key=lambda x: x[0]), headers=headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze benchmark data.")
    parser.add_argument('--mode', type=str,  choices=['repository', 'year'],
                        help="Mode of analysis: 'repository' or 'year'",default='repository')
    # parser.add_argument('--benchmark_path', type=str, required=True, help="Path to benchmark JSON file.")
    parser.add_argument('--results_path', type=str, help="Path to results JSON file.", default='agentless.eval_qwen_agentlessX.json')
    
    args = parser.parse_args()

    analyze_data(args.mode, args.results_path)