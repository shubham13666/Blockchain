import java.util.Date;

public class Block
{
    public String hash,previousHash;
    private String data;
    private long timeStamp;

    //Block Constructor
    public Block(String data, String previousHash)
    {
        this.data=data;
        this.previousHash=previousHash;
        this.timeStamp=new Date().getTime();
        this.hash = calculateHash();
    }

    public String calculateHash() 
    {
        String calculatedhash = StringToHash.StringToSHA256(
                previousHash +
                        Long.toString(timeStamp) +
                        data
        );
        return calculatedhash;
    }


}
