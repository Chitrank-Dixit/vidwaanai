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

### Verse 1 (Vishnu Puran 0.1901)
- **Original**: चत्मनेबात्म होगा और उसकी सन्तान सम्पूर्ण त्रिल्पेकीमें
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1902)
- **Original**: 58 त्वे चाप्ययोनिजा साध्वी रूपौदार्यगुणान्तिता । मन:प्रीतिकरी नृणां मत्प्रसादाद्धविष्यसि
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1903)
- **Original**: 71 इत्युक्स्वान्तर्दधे देवस्तां विशालविलोचनाम्‌। सा चेय॑ मारिषा जाता युष्पत्यत्नी नृपात्मजा:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1904)
- **Original**: 72 अऑफपराशर उवाच ततः सोमस्थ वचनाजगृहस्ते प्रचेतस: । संहत्य कोप॑ वृक्षेभ्य: पत्नीधर्मेण मारिषाम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1905)
- **Original**: 73 दरशभ्यस्तु प्रचेतोभ्यो मारिषायों प्रजापति: । जज्ञे दक्षो महाभागो य: पूर्व ब्रह्मणो3भवत्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1906)
- **Original**: 74 स तु दक्षो महाभागस्सृष्टचर्थ सुमहामते । पुत्नानुत्पादयामास प्रजासृष्टर्थमात्मनः
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1907)
- **Original**: 75 अवरांश्व वरांश्ैव द्विपदोईथ चतुष्पदान्‌। आदेश ब्रह्मण: कुर्वन सृष्टय्र्थ॑ समुपस्थित:
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1908)
- **Original**: 76 स सुप्ठा मनसा दक्ष: पश्चादसृजत खिमः । ददौ स दश् थ्र्माय कश्यपाय त्रयोदश । कालस्य नयने युक्ता: सप्तविंशतिपिन्दबे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1909)
- **Original**: 77 तासु देवास्तथा दैत्या नागा गावस्तथा खगा: । गन्धर्वाप्सरसश्ैव॒दानवाद्याश्न॒ जज्ञिरे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1910)
- **Original**: 78 ततः प्रभ्ृति मैत्रेय प्रजा मैथुनसम्भवाः। सड्डूल्पाइर्शनात्स्पर्शात्यूवेंघामभवन्‌ प्रजा: । तपोविशेषैः सिद्धानां तदात्यन्ततपस्विनाम्‌
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1911)
- **Original**: 79 श्रीमेत्रेय उदाच है, हुए कप पूर्व जातो मया शझुतः । प्राचेतसो भूयः सपुत्पन्नो महामुने
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1912)
- **Original**: 80 एघ मे संशयो ब्रह्मन्सुपहान्हदि वर्त्तते। यहौहित्रश्न सोमस्य पुनः श्वशुरतां गतः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1913)
- **Original**: 89 श्रीपराश्र उवाच उत्पत्तिश्न निरोधश्न नित्यो भूतेषु सर्वदा। ऋषयोउत्र न मुदान्ति ये चान्ये दिव्यच्षक्षुप:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1914)
- **Original**: 82 युगे युगे भक्न्त्वेते दक्षाद्या मुनिसत्तम । पुनक्षैय निरुख्धघन्ते विद्वांस्त्र न मुहाति
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1915)
- **Original**: 83 कानिष्ठ ज्यैन्‍्धमप्थेषां पूर्व नाभूदद्विजोत्तम । तप एवं गरीयो5भूत्रभावश्ैव कारणम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1916)
- **Original**: 84 अआविष्णुपुराण [ अ* 15 फैल जायगी
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1917)
- **Original**: तथा तू भी मेरी कृपासे उदाररूप- गुणसम्पन्ना, सुशील्म्र और मनुष्योंके चित्तक्ों प्रसन्न करनेवाल्ल अयोनिजा ही उत्पन्न होगी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1918)
- **Original**: हे राजपुत्रो ! उस विज्ञाल्तरक्षीसे ऐसा कह भगवान्‌ अन्तर्धान हो गये और वही यह मारिषाके रूपसे उत्पन्न हुई तुम्हारी पत्नी है
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1919)
- **Original**: श्रीपरादारजी खोले--तबर सोसदेसके कहनेसे प्रचेताओंने अपना क्रोध शान्त किया और उस मारिषाको यक्षोंसे पत्रीरूपसे ग्रहण किया
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1920)
- **Original**: उन दसों प्रचेताओंसे मारिषाके मत्यभाग दक्ष प्रजापतिका जन्म हुआ, जो पहले ब्रह्माजीसे उत्पन्न हुए ये
- **Translation**: 

---

