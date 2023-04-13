from pathlib import Path

directories = ['test_A', 'test_B']
id_by_dir = dict()
all_patient_files = list()
for directory in directories:
    # retrieve Path obj of files in each dir
    id_by_dir[directory] = list()
    patient_files = Path(directory).glob('*')
    for file in patient_files:
        # file is a Path object; cast to str
        split_by_slash = str(file).split('/')
        all_patient_files.append(str(file))
        folder = split_by_slash[0]
        patient_file = split_by_slash[1]
        fn_comps = patient_file.split('_')
        pid = fn_comps[-1]
        id_by_dir[directory].append(pid)

print(id_by_dir)
# {'test_A': ['343958030', '343980235', '4539830'], 'test_B': ['2495345', '2948298', '934292']}

ids_in_both = [pid for pid in id_by_dir['test_A'] if pid in id_by_dir['test_B']]
print(ids_in_both)  # ['123456']
id_files = dict()
for pid in ids_in_both:
    files = [file for file in all_patient_files if file.endswith(pid)]
    id_files[pid] = files
print(id_files)  # {'123456': ['test_A/pat_4_test_A_123456', 'test_B/pat_4_test_B_123456']}
for pid in id_files:
    for path in id_files[pid]:
        print(Path(path))
