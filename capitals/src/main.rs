use std::io::{self, BufRead, Write};

const CAPITALS: &[(&str, &str)] = &[
    ("Tokyo", "Japan"),
    ("Paris", "France"),
    ("Berlin", "Germany"),
    ("Ottawa", "Canada"),
    ("Canberra", "Australia"),
    ("Brasília", "Brazil"),
    ("Beijing", "China"),
    ("New Delhi", "India"),
    ("Cairo", "Egypt"),
    ("Nairobi", "Kenya"),
    ("Buenos Aires", "Argentina"),
    ("Mexico City", "Mexico"),
    ("Jakarta", "Indonesia"),
    ("Seoul", "South Korea"),
    ("Madrid", "Spain"),
    ("Rome", "Italy"),
    ("Moscow", "Russia"),
    ("Ankara", "Turkey"),
    ("Riyadh", "Saudi Arabia"),
    ("Pretoria", "South Africa"),
    ("Bangkok", "Thailand"),
    ("Warsaw", "Poland"),
    ("Lisbon", "Portugal"),
    ("Amsterdam", "Netherlands"),
    ("Stockholm", "Sweden"),
    ("Oslo", "Norway"),
    ("Helsinki", "Finland"),
    ("Vienna", "Austria"),
    ("Bern", "Switzerland"),
    ("Brussels", "Belgium"),
    ("Islamabad", "Pakistan"),
    ("Dhaka", "Bangladesh"),
    ("Kabul", "Afghanistan"),
    ("Tehran", "Iran"),
    ("Baghdad", "Iraq"),
    ("Amman", "Jordan"),
    ("Beirut", "Lebanon"),
    ("Doha", "Qatar"),
    ("Abu Dhabi", "United Arab Emirates"),
    ("Colombo", "Sri Lanka"),
    ("Kathmandu", "Nepal"),
    ("Ulaanbaatar", "Mongolia"),
    ("Hanoi", "Vietnam"),
    ("Manila", "Philippines"),
    ("Kuala Lumpur", "Malaysia"),
    ("Singapore", "Singapore"),
    ("Phnom Penh", "Cambodia"),
    ("Vientiane", "Laos"),
    ("Yangon", "Myanmar"),
    ("Accra", "Ghana"),
    ("Lagos", "Nigeria"),
    ("Addis Ababa", "Ethiopia"),
    ("Kinshasa", "Democratic Republic of the Congo"),
    ("Luanda", "Angola"),
    ("Dar es Salaam", "Tanzania"),
    ("Kampala", "Uganda"),
    ("Khartoum", "Sudan"),
    ("Rabat", "Morocco"),
    ("Algiers", "Algeria"),
    ("Tunis", "Tunisia"),
    ("Tripoli", "Libya"),
    ("Dakar", "Senegal"),
    ("Abidjan", "Ivory Coast"),
    ("Harare", "Zimbabwe"),
    ("Lusaka", "Zambia"),
    ("Maputo", "Mozambique"),
    ("Antananarivo", "Madagascar"),
    ("Santiago", "Chile"),
    ("Lima", "Peru"),
    ("Bogotá", "Colombia"),
    ("Caracas", "Venezuela"),
    ("Quito", "Ecuador"),
    ("La Paz", "Bolivia"),
    ("Asunción", "Paraguay"),
    ("Montevideo", "Uruguay"),
    ("Panama City", "Panama"),
    ("San José", "Costa Rica"),
    ("Tegucigalpa", "Honduras"),
    ("Guatemala City", "Guatemala"),
    ("Managua", "Nicaragua"),
    ("San Salvador", "El Salvador"),
    ("Havana", "Cuba"),
    ("Kingston", "Jamaica"),
    ("Port-au-Prince", "Haiti"),
    ("Santo Domingo", "Dominican Republic"),
    ("Reykjavik", "Iceland"),
    ("Dublin", "Ireland"),
    ("Athens", "Greece"),
    ("Budapest", "Hungary"),
    ("Prague", "Czech Republic"),
    ("Bucharest", "Romania"),
    ("Sofia", "Bulgaria"),
    ("Zagreb", "Croatia"),
    ("Belgrade", "Serbia"),
    ("Sarajevo", "Bosnia and Herzegovina"),
    ("Skopje", "North Macedonia"),
    ("Tirana", "Albania"),
    ("Podgorica", "Montenegro"),
    ("Pristina", "Kosovo"),
    ("Kyiv", "Ukraine"),
    ("Minsk", "Belarus"),
    ("Vilnius", "Lithuania"),
    ("Riga", "Latvia"),
    ("Tallinn", "Estonia"),
    ("Tbilisi", "Georgia"),
    ("Yerevan", "Armenia"),
    ("Baku", "Azerbaijan"),
    ("Nur-Sultan", "Kazakhstan"),
    ("Tashkent", "Uzbekistan"),
    ("Bishkek", "Kyrgyzstan"),
    ("Dushanbe", "Tajikistan"),
    ("Ashgabat", "Turkmenistan"),
];

fn shuffle<T>(slice: &mut [T]) {
    // Simple Fisher-Yates using a linear congruential generator seeded from
    // the current time — no external crates needed.
    let seed = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|d| d.subsec_nanos())
        .unwrap_or(12345) as u64;
    let mut rng = seed;
    for i in (1..slice.len()).rev() {
        rng = rng.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        let j = (rng >> 33) as usize % (i + 1);
        slice.swap(i, j);
    }
}

fn main() {
    let mut indices: Vec<usize> = (0..CAPITALS.len()).collect();
    shuffle(&mut indices);

    println!("Capitals Quiz — name the country. Type 'quit' to stop.\n");

    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let mut score = 0usize;
    let mut total = 0usize;

    for idx in indices {
        let (capital, correct) = CAPITALS[idx];
        print!("{capital}: ");
        io::stdout().flush().unwrap();

        let answer = match lines.next() {
            Some(Ok(line)) => line,
            _ => break,
        };

        if answer.trim().to_lowercase() == "quit" {
            break;
        }

        total += 1;
        if answer.trim().to_lowercase() == correct.to_lowercase() {
            score += 1;
            println!("Correct!");
        } else {
            println!("Wrong — {correct}");
        }
    }

    if total > 0 {
        println!("\n{score}/{total}");
    }
}
