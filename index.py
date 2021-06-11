from pprintpp import pprint as pp
from functional import seq
import click, os

def range_n(end):
  return list(range(1, end + 1))

def gen_string(string, suffix, zero_count = 3):
  return str(string).zfill(zero_count) + suffix

def rename_file (file_path, src, dist):
  src_path = os.path.join(file_path, src)
  dist_path = os.path.join(file_path, dist)
  print('> src_path:\n', src_path)
  print('> dist_path:\n', dist_path)
  return os.rename(src_path, dist_path)

@click.command()
@click.option('-p', '--path', prompt='File location', help="Music files location")
@click.option('-s', '--suffix', prompt='File name suffix', help="File name suffix") # 숫자 제외한 반복되는 문자열
def main(path, suffix):
  src_file_names = os.listdir(path)
  ranger = [gen_string(x, suffix) for x in range_n(100)]
  dist_file_names = list(map(lambda x: x.replace(list(filter(lambda y: y in x, ranger))[0] if list(filter(lambda y: y in x, ranger)) else '', ''), src_file_names))
  
  print('> dist_file_names:\n', dist_file_names)
  list(map(lambda x, y: rename_file(path, x, y), src_file_names, dist_file_names))

if __name__ == "__main__":
  main()