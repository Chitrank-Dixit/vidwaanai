# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vishnu Puran 0.501)
- **Original**: आन्ध ] अधम अंश श्र श्रापदा द्विखुरा हस्ती बानरा: पक्षिपक्लमाः । औदका: पहावः षष्ठाः सप्तमास्तु सरीसुपा:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.502)
- **Original**: 52 गायत्र॑ च ऋचश्णैव त्रिवृत्सोम॑ रथन्तरम्‌। अस्िष्टोम॑ च यज्ञानां निर्मम प्रथमान्मुखात्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.503)
- **Original**: 53 यजूंषि त्रैष्टभ॑ छन्दः स्तोर्म पदश्चद्॒श तथा । बृहत्साम तथोक्‍्थं जन दक्षिणादसृजन्पुखात्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.504)
- **Original**: 54 साम्तानि जगतीछन्द: स्तोम॑ सप्तदश तथा । वैरूपमतिरात्र चर पश्चिमादसृजन्युखात्‌ । 55 एकबिंशमधर्वाणमाप्तोर्यामाणमेतब॒ तन । अनुष्ठुभ॑ च बैराजमुत्तरादसृजन्मुखात्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.505)
- **Original**: 56 उच्चावच्ानि भूतानि गात्रेभ्यस्तस्य जज्ञिरे। देवासुरपितुन्‌ सृष्टूखा मनुष्यांश्र प्रजापति:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.506)
- **Original**: तत: पुनः ससर्जाद्े सड्डूल्पस्य पितामह: । यक्षान्‌ पिशाचान्गश्थर्वान्‌ तथैवाप्सरसां गणान्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.507)
- **Original**: 58 नरकिन्नररक्षांसि बयय: पशुमृगोरगान्‌ । अव्ययं चञ्ञ व्यवं चैव यदिदं स्थाणुजड्रमम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.508)
- **Original**: 59 तत्ससर्ज तदा ब्रह्मा भगवानादिकृत्मभु: । तेषां ये यानि कर्माणि प्राक्सृष्टयां प्रतिपेदिरे । तानयेव ते प्रपद्चन्ते सृज्यमाना: पुनः पुन;
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.509)
- **Original**: 60 हिंस्राहिस्ने मृदुकूरे धर्माधर्मावृतानृते । तद्भाबिता: प्रपद्चन्ते तस्मात्तत्तस्य रोचते
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.510)
- **Original**: 69 इन्द्रियार्थेषु भूतेषु शरीरेषु ल स प्रभु: । नानात्व बिनियोगं च धातैव॑ व्यसृजत्स्वयम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.511)
- **Original**: 62 जाम रूप॑ च॒ भूतानां कृत्यानां च प्रपक्चननम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.512)
- **Original**: वेदशब्देभ्य एवादौ देवादीनां चकार सः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.513)
- **Original**: 63 ऋषीणां नामधेयात्रि यथा वेदश्रुतानि वै। तथा नियोगयोम्यानि ह्ान्येषामपि सोउकरोत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.514)
- **Original**: 64 32. +.# नानारूपाणि पर्यवे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.515)
- **Original**: तानि तान्येव तथा भावषा युगादिषु
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.516)
- **Original**: 65 करोत्येवविधां सृष्टि कल्पादौ स पुनः पुनः । सिसृक्षाशक्तियुक्तोडसो. सृज्यशक्तिप्रचोदितः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.517)
- **Original**: 66 गाँवॉमें रहनेनाले पशु हैं। जंगली पशु ये ऐं---श्रापद (व्याप्न आदि), दो खुरखाले (बनगाय आदि), हाथी, बन्दर और पाँचयें पक्षी, छठे जलके जीव तथा सातवें सरोसप आदि
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.518)
- **Original**: फिर अपने प्रथम (पूर्व) मुखसे ऋद्माजीने गायत्री, ऋचु, त्रिवृत्सोम रथन्तर और अग्रिप्टोम यज्ञोंको निर्मित किया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.519)
- **Original**: दक्षिण-मुखसे यु, त्ष्टपक़न्द, पश्रदशास्तोम, बृहत्साम तथा उक्थकी रचना ट्गै
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.520)
- **Original**: पश्चिम-मुख्से साम, जगतीछन्द, सप्तददास्तोम, चैरूप और अतिरात्रकों उत्पन्न किया
- **Translation**: 

---

