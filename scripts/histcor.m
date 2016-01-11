function cor = histcor(img)

for i=1:256
h(i) = sum(sum(img==i-1));
end

cor = img;
s = sum(h);

for i = 1:256
I = find(img==i-1);
cor(I) = sum(h(1:i))/s*255;
end
 