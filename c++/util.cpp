//최대공약수
int gcd(int a, int b){
  while (b > 0){
    int temp = b;
    b = a % b;
    a = temp;
  }
  return a;
}

//최소공배수
int lcm(int a, int b){
  return (a * b) / gcd(a, b);
}

// pair배열 오름차순
bool compare(const pair<int, int>& a, const pair<int,int>& b){
    if(a.first == b.first)
        return a.second < b.second;
    return a.first <b.first;
}



//lower_bound (찾으려 하는 key 값이 없으면 key 값보다 큰 가장 작은 정수의 인덱스)
//stl ex) lower_bound(arr, arr + 10, 6)
int lower_bound(int *arr, int n, int key){ // n = 배열 수
  int start = 0;
  int end = n - 1;
  int mid;
  while (end > start)
  {                          //start 가 end 와 같지 않고, 넘지 않을 때
    mid = (start + end) / 2; //중앙 index

    if (arr[mid] < key)
    {                  //key 값이 중앙 값보다 크면
      start = mid + 1; //mid 보다 오른쪽으로
    }
    else
    {            //key 값이 중앙값보다 작거나 같으면
      end = mid; //mid 포함 왼쪽 (포함하는 이유는 key값과 같은게 없을 때 큰수중 가장 작은값을 위해)
    }
  }
  return end + 1;
}

//upper_bound (key값을 초과하는 가장 작은 정수의 인덱스)
//stl ex) upper_bound(arr, arr + 10, 6)
int upper_bound(int *arr, int n, int key){
  int start = 0;
  int end = n - 1;
  int mid;

  while (end > start){
    mid = (start + end) / 2;

    if (arr[mid] <= key){ //lower_bound와 다른 점은 여기 '=' 하나
      start = mid + 1;
    }
    else{
      end = mid;
    }
  }

  return end + 1;
}
