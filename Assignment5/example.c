public static double ReturnAverage(int value[], int AS, int MIN, int MAX) {
    int i, ti, tv, sum;
    double av;
    i = 0; ti = 0; tv = 0; sum = 0;
    while (ti < AS && value[i] != -999) {
        ti++;
        if(value[i] >= MIN && value[i] <= MAX) {
            tv++;
            sum = sum + value[i];
        }
        i++;
    }
    if (tv > 0)
        av = (double) sum/tv;
    else
        av = (double) -999;
    return (av);
}


