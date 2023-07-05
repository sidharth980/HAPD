#include <stdio.h>
#include <stdlib.h>

typedef struct {
    float vel;
    int n;
    float pos;
} kfilter;

void init(kfilter *kf) {
    kf->vel = 0;
    kf->n = 1;
    kf->pos = 0;
}

float predict(kfilter *kf, int pos) {
    if (kf->vel == 0) {
        return 0;
    }
    if (pos == 0) {
        kf->n = 0;
        return kf->vel + kf->pos;
    } else {
        kf->pos = kf->pos + kf->vel;
        return kf->pos + kf->vel;
    }
}

float update(kfilter *kf, float x) {
    if (x == 0) {
        return predict(kf, kf->n);
    } else {
        if (kf->vel == 0) {
            if (kf->pos != 0) {
                kf->vel = x - kf->pos;
            }
            kf->pos = x;
            return predict(kf, kf->n);
        } else {
            float est_pos = predict(kf, 0);
            float dif = (est_pos - x) / 1.25;
            kf->vel = kf->vel - dif;
            kf->pos = x;
            return predict(kf, kf->n);
        }
    }
}

int main() {
    kfilter kf;
    init(&kf);
    for(int x = 0;x<10;x++){
    float result = update(&kf, x);
    printf("%f\n",result);
    }
    return 0;
}

