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

### Verse 1 (Bramha 0.7701)
- **Original**: पड़े हों, जिसे कुत्तेने देखा अथवा चाट लिया हो और गुरु-इनको दाहिने करके चले। दूसरॉके
- **Translation**: 

---

### Verse 2 (Bramha 0.7702)
- **Original**: अथवा जो सारभाग निकाल लेनेके कारण दूषित धारण किये हुए जूते, वस्त्र और माला आदि स्वयं
- **Translation**: 

---

### Verse 3 (Bramha 0.7703)
- **Original**: हो गया हो, ऐसे अन्नको कभी न खाय। भोजनके न पहने। चतुर्दशी, अष्टमी, पूर्णिमा तथा पर्वके
- **Translation**: 

---

### Verse 4 (Bramha 0.7704)
- **Original**: साथ अलग नमक रखकर न खाय। बहुत देरके दिन तैलाभ्यड्भ एवं स्त्री-सहवास न करे। बुद्धिमान्‌
- **Translation**: 

---

### Verse 5 (Bramha 0.7705)
- **Original**: बने हुए सूखे और बासी अन्नको त्याग दे। पिट्टी, मनुष्य बाँहों और पिंडलियोंको ऊपर उठाकर न साग, ईखके रस और दूधकी बनी हुई बस्तुएँ भी खड़ा हो तथा पैरोंको भी न हिलाये। पैरसे पैरको
- **Translation**: 

---

### Verse 6 (Bramha 0.7706)
- **Original**: यदि बहुत दिनोंकी हों तो उन्हें न खाय। सूर्यके न दबाये। किसीको चुभती हुई बात न कहे।
- **Translation**: 

---

### Verse 7 (Bramha 0.7707)
- **Original**: उदय और अस्तके समय शयन न करे। बिना निन्‍दा और चुगली छोड़ दे। दम्भ, अभिमान और
- **Translation**: 

---

### Verse 8 (Bramha 0.7708)
- **Original**: नहाये, बिना बैठे, अन्यमनस्क होकर, शब्यापर तीखे व्यवहारका त्याग करे। मूर्ख, उन्मत्त, व्यसनी,
- **Translation**: 

---

### Verse 9 (Bramha 0.7709)
- **Original**: बैठकर या सोकर, केवल पृथ्वीपर बैठकर, कुरूप, हीनाड़् और निर्धन मनुष्योंकी खिल्ली न
- **Translation**: 

---

### Verse 10 (Bramha 0.7710)
- **Original**: बोलते हुए तथा भृत्यवर्गको दिये बिना कदापि उड़ाये। दूसरेको दण्ड न दे, केबल पुत्र और
- **Translation**: 

---

### Verse 11 (Bramha 0.7711)
- **Original**: भोजन न करे। मनुष्य स्तरान करके सबेरे और शिष्यको शिक्षा देनेके उद्देश्यसे दण्ड दिया जा
- **Translation**: 

---

### Verse 12 (Bramha 0.7712)
- **Original**: शाम दो समय विधिपूर्वक भोजन करे। सकता है। आसनको पैरसे खींचकर न बैठे।। विद्वान्‌ पुरुषकों कभी परायो स्त्रीके साथ सायंकाल और प्रात:काल पहले अतिधिका सत्कार
- **Translation**: 

---

### Verse 13 (Bramha 0.7713)
- **Original**: समागम नहीं करना चाहिये
- **Translation**: 

---

### Verse 14 (Bramha 0.7714)
- **Original**: परस्त्रीसंगम मनुष्योंके करके पीछे स्वयं भोजन करे।
- **Translation**: 

---

### Verse 15 (Bramha 0.7715)
- **Original**: इष्ट, पूर्त और आयुका नाश करनेवाला है। इस पूर्व या उत्तकी ओर मुँह करके ही दाँतन
- **Translation**: 

---

### Verse 16 (Bramha 0.7716)
- **Original**: संसारमें परस्त्री-गमनके समान पुरुषकी आयुका करे। दाँतन करते समय मौन रहे। दाँतनके लिये
- **Translation**: 

---

### Verse 17 (Bramha 0.7717)
- **Original**: विधातक कार्य दूसरा कोई नहीं है।* देवपूजा, निषिद्ध वृक्ष एवं लताओंका परित्याग करे। उत्तर
- **Translation**: 

---

### Verse 18 (Bramha 0.7718)
- **Original**: अग्निहोत्र, पितरोंका श्राद्ध, गुरुजनोंको प्रणाम तथा और पश्चिमकी ओर सिर करके कभी न सोये।
- **Translation**: 

---

### Verse 19 (Bramha 0.7719)
- **Original**: भोजन भलोभाँति आचमन करके करना चाहिये। दक्षिण या पूर्व दिशाकौ ओर ही मस्तक करके
- **Translation**: 

---

### Verse 20 (Bramha 0.7720)
- **Original**: स्वच्छ, फेनरहित, दुर्गन्‍्धशून्य और पवित्र जल सोना चाहिये। जहाँसे दुर्गनध आती हो, ऐसे लेकर पूर्व या उत्तरकी ओर मुँह करके आचमन जलमें तथा रात्रिकालपें स्नान न करे। ग्रहणके
- **Translation**: 

---

