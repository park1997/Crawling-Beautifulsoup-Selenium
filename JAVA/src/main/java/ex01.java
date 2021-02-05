import org.json.simple.JSONArray;
import org.json.simple.JSONObject;


public class ex01 {
    public static void main(String[] args) {
        JSONObject info = new JSONObject();
        JSONArray arr = new JSONArray();
        JSONObject detail = new JSONObject();

        arr.add("11");
        arr.add("12");
        System.out.println(arr);

        detail.put("num",arr);
        info.put("단지내면적별정보", detail);

        System.out.println(info);
        System.out.println(info.get("단지내면적별정보"));
        System.out.println(info.get("단지내면적별정보").toString());
        JSONObject object = (JSONObject) info.get("단지내면적별정보");

        System.out.println(object.get("num"));

        info.put("하이", detail.put("num", "arr"));
        System.out.println(info);
        info.put("단지내면적별정보", detail.put("num", arr));
        System.out.println(info);


    }
}
