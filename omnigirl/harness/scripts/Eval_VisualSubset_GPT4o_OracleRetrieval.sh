METHOD="oracle_retrieval"
MODEL="GPT-4o-2024-08-06"

idx=("0" "1" "2")


settings=("text_only" "text_image" "image_augmented_text")


for idx in "${idx[@]}"; do
    for setting in "${settings[@]}"; do
        python run_evaluation.py --dataset_name benchmark/OmniGIRL.json --predictions_path patch/visual_subset/${MODEL}/${METHOD}/${setting}/patch${idx}.jsonl --max_workers 20 --run_id eval_visual_subset_gpt4o_${METHOD}_${setting}_${idx}
     
    done
done
