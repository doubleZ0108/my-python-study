def imshift(frame, dx, dy):
    '''
    图像平移
    
    向右dx个像素
    向下dy个像素
    '''
    M, N = frame.shape[:2]
    A = np.float32([[1, 0, dx], [0, 1, dy]])
    shifted_frame = cv2.warpAffine(frame, A, (N, M))
    return shifted_frame
    
