def write_CPLEX_dat(file_name, T, varDim, constrDimH, constrDimG, G, H, alpha, a, b, gamma, c )
    fileID = fopen(file_name,'w');
    fprintf(fileID,'T = %6.2f;\r\n',T);
    fprintf(fileID,'VarDimension = %8u;\r\n',varDim);
    fprintf(fileID,'ConstrDimensionH = %8u;\r\n',constrDimH);
    fprintf(fileID,'ConstrDimensionG = %8u;\r\n',constrDimG);
    [row, col] = size(G);
    fprintf(fileID,'G = {\r\n');
    for i = 1:row
        for j = 1:col
            if ~ G(i,j)==0
                fprintf(fileID,'<%8u %8u %8g>\r\n',i, j, G(i,j));
            end
        end
    end
    fprintf(fileID,'};\r\n\r\n');
    fprintf(fileID,'H = {\r\n');
    [row, col] = size(H);
    for i = 1:row
        for j = 1:col
            if ~ H(i,j)==0
                fprintf(fileID,'<%8u %8u %8g>\r\n',i, j, H(i,j));
            end
        end
    end
    fprintf(fileID,'};\r\n\r\n');
    fprintf(fileID,'alpha = {\r\n');
    for i = 1:length(alpha)
        if ~ alpha(i)==0
            fprintf(fileID,'<%8u %8u %8g>\r\n',i, 1, alpha(i));
        end
    end
    fprintf(fileID,'};\r\n\r\n');
    fprintf(fileID,'a = {\r\n');
    for i = 1:length(a)
        if ~ a(i)==0
            fprintf(fileID,'<%8u %8u %8g>\r\n',i, 1, a(i));
        end
    end
    fprintf(fileID,'};\r\n\r\n');
    fprintf(fileID,'b = {\r\n');
    for i = 1:length(b)
        if ~ b(i)==0
            fprintf(fileID,'<%8u %8u %8g>\r\n',i, 1, b(i));
        end
    end
    fprintf(fileID,'};\r\n\r\n');
    fprintf(fileID,'c = {\r\n');
    for i = 1:length(c)
        if ~ c(i)==0
            fprintf(fileID,'<%8u %8u %8g>\r\n',i, 1, c(i));
        end
    end
    fprintf(fileID,'};\r\n\r\n');
    fprintf(fileID,'gamma = {\r\n');
    for i = 1:length(gamma)
        if ~ gamma(i)==0
            fprintf(fileID,'<%8u %8u %8g>\r\n',i, 1, gamma(i));
        end
    end
    fprintf(fileID,'};\r\n\r\n');
    fclose(fileID);
    end