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

### Verse 1 (Vishnu Puran 0.1921)
- **Original**: है महामते ! उन महाभाग दक्षने, बरह्माजीयी आज्ञा पालते हुए सर्ग-रचनाके लिये उद्यत होकर उनकी अपनी सृष्टि बढ़ाने और सन्तान उत्पन्न करनेके लिये नीच-कँच तथा द्विपदलत॒ष्पद आदि नाना प्रकारके जीवोंको पुत्ररूपसे उत्पन्न किया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1922)
- **Original**: प्रजापति दक्षने पहले मनसे ही सृष्टि करके फिर स्त्रियोंकी उत्पत्ति की । उनमेंसे दस धर्मको और तेरह कश्यफ्को दीं तथा काऊ-परिवर्तनमें नियुक्त (अश्विनी आदि] सत्ताईस चन्द्रमाकों त्रिचाह दीं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1923)
- **Original**: उन्हींसे देवता, दैत्य, नाग, गौ, पक्षी, गन्धर्व, अप्सरा और दानव आदि उत्पन्न हुए
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1924)
- **Original**: हे मैत्रेय
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1925)
- **Original**: दक्षके समयसे ही प्रजाका मैथुन (स्त्री-पुरुष-सम्बन्ध) द्वारा उत्पन्न होना आरम्भ हुआ है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1926)
- **Original**: उससे पहले तो अत्यन्त तपस्वी प्राचीन सिद्ध पुरुषोंके तपोबलसे उनके संकल्प, दर्शन अथवा स्पर्यामाजसे ही प्रजा उत्पन्न होती थी
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1927)
- **Original**: अमैत्रेयजी बोले--हे महामुने ! मैंने तो सुना था कि दक्षका जन्म बद्याजीके दायें अगूठेसे हुआ था, फिर ये प्रचेताओंके पुत्र किस प्रकार हुए 7
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1928)
- **Original**: हे ब्रह्मन्‌ ! मेरे हृदयमें यह बड़ा सन्देह है कि सोमदेवके दौहित्र (घेवते) होकर भी फिर वे उनके धशुर हुए !
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1929)
- **Original**: श्रीपरावारजी बोले--हे मैत्रेय ! प्राणियोंके उत्पत्ति और नाश ( भ्रवाहरूपसे ] निर्तर हुआ करते हैं। इस विषयमें ऋषियों तथा अन्य दिव्यदृष्टि-पुरुषोंक क्व्रेई मोह नहीं होता
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1930)
- **Original**: हे पुनिश्रेष्ठ ! ये दक्षादि युग-युगमें होते हैं और फिर लीन हो जाते हैं; इसमें विद्वान्‌को किसी प्रकारका सन्‍्देह नहीं होता
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1931)
- **Original**: हे ड्विजोत्तम ! इनमें पहले किसी प्रकारकी ज्येप्रता अथवा कनिष्ठता भी नहीं थी। उस समय तप और प्रभाव ही उनकी ज्येहताका कारण होता था
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1932)
- **Original**: आ0 175 ] ओमैष्रेय उताच देवानां दानवानां चर गन्धर्वोरिगरक्षसाप्‌ उत्पत्ति विस्तरेणेह मम ब्रह्मन्प्रकीत्तय
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1933)
- **Original**: 85 अऔपराशर उवाच प्रजा: सृजेति व्यादिष्ट: पूर्व दक्ष: स्वयम्भुवा । यथा ससर्ज भूतानि तथा श्रृणु महामुने
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1934)
- **Original**: 86 मानसान्येव भूतानि पूर्व दक्षोडसृजत्तदा । देवानृषीन्सगन्धर्वानसुरान्पन्नगांस्तथा._
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1935)
- **Original**: 87 यदास्य सृजमानस्य न व्यवर्धन्तत ता: प्रजा: । ततः सझ्िन्त्य स पुनः सृष्टिहेतो: प्रजापति:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1936)
- **Original**: 88 मैथुनेनेव धर्मेण सिसृक्षुर्विविधा: प्रजा: । असिक्कीमावहत्कन्यां वीरणस्य प्रजापते: । सुतां सुतपसा युक्तां महती ल्त्रेकधारिणीम्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1937)
- **Original**: 89 अध पुत्रसहस्नाणि वैरुण्यां पश्च वीर्यवान्‌। असिकक्‍नयां जनयामास सर्गहितोः प्रजापति:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1938)
- **Original**: 90 तान्दृष्ठा नारदो विष्र संविवर्द्धयिषूत्रजा: । सड्रम्य॒प्रियसंवादो देवर्षिरिदमब्रवीत
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1939)
- **Original**: 91 हे हर्यश्वा महावीर्या: प्रजा यूयं करिष्यथ । ईदुशो दृश्यते यत्नो भवतां श्रूयतामिदम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1940)
- **Original**: 92 बालिज्ञा बत यूय॑ वे नास्या जानीत वे भुव: । अन्तरूधध्वमधश्चैव॒ कर्थ सुक्ष्यथ वै प्रजा:
- **Translation**: 

---

