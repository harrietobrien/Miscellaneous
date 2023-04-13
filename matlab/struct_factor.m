%27-201 HW 4 Question 2

coords=[0,0,0];
XYcoords=[0,0];

for h=-4:4
    for k=-4:4
        for l=-4:4
            structFactF=1+mod(h+k,2)+mod(k+l,2)+mod(h+l,2);
            if structFactF==1 && h+k+l==0
                signH=1;
                if l<0
                    signH=-1;
                end
                spacing=1/(((h^2+k^2+l^2)/(3.54E-10)^2)^0.5);
                magni=1/spacing;
                vectorMag=sqrt(h^2+k^2+l^2);
                mag220=sqrt(8);
                angle=acos(1/vectorMag*1/mag220*(2*h-2*k));
                x=magni*cos(angle);
                y=signH*magni*sin(angle);
                coords=vertcat(coords,[h,k,l]);
                XYcoords=vertcat(XYcoords,[x,y]);
            end
        end
    end
end

labels=cellstr(num2str((coords)));
figure;
plot(XYcoords(:,1),XYcoords(:,2),'o','MarkerSize',6,'MarkerEdgeColor','black','MarkerFaceColor','black')
title('Intensity-Weighted Reciprocal Lattice: FCC [111]')
text(XYcoords(:,1)+0.08E10,XYcoords(:,2),labels,'FontSize',9)
text(XYcoords(:,1)+0.275E10,XYcoords(:,2),'*','FontSize',14)
%%
coords=[0,0,0,0];
XYcoords=[0,0];
structFacts=[0];

for h=-3:3
    for k=-3:3
        for l=-3:3
            intensityH=4*(cos(pi*((h+2*k)/3+l/2)))^2;
            if structFactH~=0 && l==0
                structFacts=vertcat(structFacts,[intensityH]);
                i=-(h+k);
                signX=1;
                if k<0
                    signX=-1;
                end
                spacing=1/((4/3*((h^2+k^2+h*k)/(2.5E-10)^2)+l^2/(4.07E-10)^2)^0.5);
                magni=1/spacing;
                vectorMag=sqrt(h^2+k^2+i^2);
                mag1010=sqrt(2);
                angle=acos(1/vectorMag*1/mag1010*(h-i));
                x=signX*magni*cos(angle-pi/2);
                y=magni*sin(angle-pi/2);
                coords=vertcat(coords,[h,k,i,l]);
                XYcoords=vertcat(XYcoords,[x,y]);
            end
        end
    end
end

XY4coords=[0,0];

for i=1:50
    if structFacts(i)==4
        XY4coords=vertcat(XY4coords,[XYcoords(i,:)]);
    end
end
labels=cellstr(num2str((coords)));
figure;
plot(XYcoords(:,1),XYcoords(:,2),'o','MarkerSize',3,'MarkerEdgeColor','black','MarkerFaceColor','black')
hold on;
plot(XY4coords(:,1),XY4coords(:,2),'o','MarkerSize',8,'MarkerEdgeColor','black','MarkerFaceColor','black')
title('Intensity-Weighted Reciprocal Lattice: HCP [0001]')
text(XYcoords(:,1)+0.08E10,XYcoords(:,2),labels,'FontSize',12)
text(XYcoords(:,1)+0.25E10,XYcoords(:,2),'*','FontSize',16)



