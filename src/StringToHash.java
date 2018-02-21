import java.security.MessageDigest;

public class StringToHash
{
    // Converts String data to SHA-256 hash

    public static String StringToSHA256(String input)
    {
        try
        {
            MessageDigest digest=MessageDigest.getInstance("SHA-256");
            byte hash[]=digest.digest(input.getBytes("UTF-8"));
            StringBuffer hexString = new StringBuffer(); // This will contain hash as hexadecimal

            for (int i = 0; i < hash.length; i++)
            {
                String hex = Integer.toHexString(0xff & hash[i]);
                if(hex.length() == 1)
                    hexString.append('0');
                hexString.append(hex);
            }

            return hexString.toString();
        }
        catch(Exception e) {
            throw new RuntimeException(e);
        }
    }

}
