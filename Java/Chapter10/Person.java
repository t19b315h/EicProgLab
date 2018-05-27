public class Person {

    private String _name;
    private String _konomi;
    public String kibun = "普通";
    
    public Person(String name, String konomi) {
        this._name = name;
        this._konomi = konomi;
    }
    
    public void listenToMusic(CdPlayer cdPlayer) {
	String genre = cdPlayer.playCd();
        if (genre.equals(this._konomi))
	    this.kibun = "楽しい";
        else 
	    this.kibun = "イライラ";
    }

}
