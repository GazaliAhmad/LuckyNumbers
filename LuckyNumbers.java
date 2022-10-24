import static java.lang.System.out;
import static java.text.MessageFormat.format;

public class LuckyNumbers {
	
	public static void main(String[] args) {
		out.println(format("\nLucky 4D numbers: {0}", draw4d()));
		out.println(format("\nLucky Toto numbers: {0}", drawToto()));
	}
	
	private static String draw4d() {
		var lucky4d = new int[4];
		var i = 0;
		while (i < lucky4d.length) {
			lucky4d[i] = (int) (Math.random() * 10);
			i++;
		}
		return "%d%d%d%d".formatted(lucky4d[0],
				lucky4d[1],
				lucky4d[2],
				lucky4d[3]);
	}
	private static String drawToto() {
		var luckyToto = new int[6];
		var i = 0;
		while (i < luckyToto.length) {
			luckyToto[i] = (int) (Math.random() * 49 + 1);
			i++;
		}
		return "%02d %02d %02d %02d %02d %02d\n".formatted(luckyToto[0],
				luckyToto[1],
				luckyToto[2],
				luckyToto[3],
				luckyToto[4],
				luckyToto[5]);
	}
}