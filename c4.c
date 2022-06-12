int fb(int x);
int fb(int x)
{
    if (x <= 2)
    {
        return 1;
    }
    else
    {
        return fb(x-2)+fb(x-1);
    };    
}
