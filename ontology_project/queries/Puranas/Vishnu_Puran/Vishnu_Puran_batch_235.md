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

### Verse 1 (Vishnu Puran 0.4681)
- **Original**: 20 पारा मरीचिगर्भाश् सुधर्माणस्तथा त्रिधा । भविष्यन्ति तथा देवा होकैको द्वादशों गण:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4682)
- **Original**: 21 तेषामिन्द्रो महालीयों भविष्यत्यद्भुतो द्विज
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4683)
- **Original**: 22 सवनो द्युतिपान्‌ भव्यो वसुर्मेधातिधिस्तथा । ज्योतिष्मान सप्तमः सत्यस्तत्रेते चर महर्घय:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4684)
- **Original**: 23 धृतकेतुर्दीपिकेतु:-.. पश्चहस्तनिरामयों । पृथुश्रवाद्याश्न तथा दक्षसावर्णिकात्मजा:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4685)
- **Original**: 24 दशमो ब्रह्मसावर्णिभभविष्यति मुने मनुः । सुधामानों विशुद्धाश्ष शतसंख्यास्तथा सुराः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4686)
- **Original**: 25 तृतीय अंश 167 तथा विश्वकर्मनि उनके तेजकों शान्त कर दिया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4687)
- **Original**: उन्होंने सूर्यकों भ्रमियन्‍त्र (सान) पर चढ़ाकर उनक्रा तेज छॉटा, किन्तु ने उस अक्षुण्ण त्तेजका केचल अष्टमांश ही क्षीण कर सके
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4688)
- **Original**: हे मुनिसत्तम ! सूर्यके जिस जाज्वल्यमान कैष्णब-तेजको चविश्वकर्मने छाँठा था वह पृथिवीपर गिरा
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4689)
- **Original**: उस पृथिवीपर गिरे हुए सूर्य- तेजसे ही निः्चकर्गने विष्णुभगवानक्र चक्र, वाद्भूरका अन्य देवताओंके भी जो-जो शास्त्र थे उन्हें उसरो पुष्ट किया
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4690)
- **Original**: जिस झ्मयासंशाके पुत्र दूसरे मनुका ऊपर वर्णन कर चुके हैं वह अपने अग्रज मनुका सवर्ण होनेसे सार्वार्ण कहल्थया
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4691)
- **Original**: है महाभाग! सुनो, अब मैं उनके इस सार्वार्णकनाम आठवें मन्वन्तरका, जो आगे होनेब्राला है, बर्णन करता हूँ
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4692)
- **Original**: हे मैत्रेय ! यह साबर्णि ही ठस्त समय मनु होंगे तथा सुतप, अमिताभ और मुख्यगण देवता होंगे
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4693)
- **Original**: उन देवताओंका प्रत्येक गण बीस-औसका समूह कहा जाता है। हे मुनिसत्तम ! अब मैं आगे होनेवाले सप्तर्षि भी नतलाता हूँ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4694)
- **Original**: उस समय दीप़िमान, गाव, राप, कप, द्रोण-पुत्र अश्वस्थामा, मेरे पुत्र व्यास और सातवें ऋष्यथ॒द्ध--ये सप्र्षि होंगे
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4695)
- **Original**: तथा पाताऊ-ल्मेकबासी विरेचनके पुत्र बलि श्रीकिष्णुभगवान्‌की कपासे तत्कालीन इन्द्र और सायर्णिमनुके पुत्र चिरजा, उर्यरीवान्‌ एव निर्मोक आदि तत्कालीन राजा होंगे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4696)
- **Original**: हे मुने । नें मनु दक्षसार्वार्ण होंगे। उनके समय पार, फरीचिगर्भ और सुधर्मा नामक तोन देववर्ग होंगे जिनमेंसे भत्येक बर्गमे बारह-बारह देवता होंगे; तथा हे द्विज ! उनका नायक महाएपराक्रमी अद्भुत नामक इच्ध होगा
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4697)
- **Original**: 20--22
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4698)
- **Original**: सथन, च्ुतिमान्‌, भव्य, वसु, मैघातिथि, ज्योतिष्मान्‌ और सातयें सत्य--ये उस समयके सप्तर्षि होंगे
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4699)
- **Original**: तथा धृतकेतु, दीप्तिकेतु पञ्चहस्त, निरामय ओर पृथुश्रषा आदि दक्षसाबर्णिमनुके पुत्र होंगे
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4700)
- **Original**: है मुने । दसतें मनु अ्ह्मसावर्णि हॉंगें। उनके समय
- **Translation**: 

---

