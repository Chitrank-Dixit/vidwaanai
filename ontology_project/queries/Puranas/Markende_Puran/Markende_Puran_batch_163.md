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

### Verse 1 (Markende Puran 0.3241)
- **Original**: तत्त: सिंहश्चस्वाढ़ोग्रं * दुद्वाक्षुणणशिरौधरान्‌। असुरांस्तास्तथा काली शिवदूती तथापरान्‌
- **Translation**: 

---

### Verse 2 (Markende Puran 0.3242)
- **Original**: कौंप्ारीशक्तिनिर्भिन्ना: केचित्रेशुर्महासुसः। ब्ह्माणीमन्रपूतेत तोयेनान्ये निराकृताः
- **Translation**: 

---

### Verse 3 (Markende Puran 0.3243)
- **Original**: माहैश्नरीप्रिशुलेन भिन्ना: पेतुस्तशापरे। बाराहीतुण्डघातेन केचिच्चूर्णीकृता भुत्रि
- **Translation**: 

---

### Verse 4 (Markende Puran 0.3244)
- **Original**: खएड* खण्ड च चक्रेण वैष्णाव्या दानवाः कृता: । बजेण चैद्रीहस्ताग्रलिमुक्तेन तथापरे।
- **Translation**: 

---

### Verse 5 (Markende Puran 0.3245)
- **Original**: क्रेचिद्विनेशुरसुरा: केचिन्नप्टा महाहवात्‌। भक्षिताश्वापेर कालीशिबदूती मुगाधिप: 320
- **Translation**: 

---

### Verse 6 (Markende Puran 0.3246)
- **Original**: इतनेमें ही निशुम्पकों चेतना हुई और उसने धनुष हाथमें लेकर बा्णोंद्वारा देवी, काली तथा सिंहकों घावल कर डाला
- **Translation**: 

---

### Verse 7 (Markende Puran 0.3247)
- **Original**: फिर डस दैत्यगाजने दस हजार बाँहें बनाकर चक्रोंके प्रहारसे चाण्डिकाको आच्छादित कर दिया
- **Translation**: 

---

### Verse 8 (Markende Puran 0.3248)
- **Original**: तब दुर्गमभ पोड़ाका नाश करनेज्राली भगज्तों दुगनि कुपित होकर अपने बाणोंसे उन चक्रों तथा
- **Translation**: 

---

### Verse 9 (Markende Puran 0.3249)
- **Original**: 225 + सींक्षप्त मा्कंणदेयप्राण + 390»232250:77:54248##6 &$7 5
- **Translation**: 

---

### Verse 10 (Markende Puran 0.3250)
- **Original**: 2:55 45:56 & #4#01707 74473: #4+*0 20 2236. 66% 0-7 ज कह श/अयय 86 #-#5 005 करू बाणोंकों काट गिराबा
- **Translation**: 

---

### Verse 11 (Markende Puran 0.3251)
- **Original**: यह देख निशुश्भ गर्दग कुचलकर खाने लगा, वह बड़ा भय॑क्वर दृश्य दैत्यसेनाक्रे साथ चेणिडकाका वध करनेफे लिये
- **Translation**: 

---

### Verse 12 (Markende Puran 0.3252)
- **Original**: धा। उधर काली तथा शिवदूतीने भी अन्यान्य हाथपें गदा ले बड्धे बेगसे दौड़ा
- **Translation**: 

---

### Verse 13 (Markende Puran 0.3253)
- **Original**: उसके आते
- **Translation**: 

---

### Verse 14 (Markende Puran 0.3254)
- **Original**: दैत्यॉँका भक्षण आर»्ध किया
- **Translation**: 

---

### Verse 15 (Markende Puran 0.3255)
- **Original**: कौमारीको हो चण्डीने तोखी धारवाली त्तलवास्से उसकी गदाको 2 “# हर शीघ्रही काट डला। तन उसने शूल हाथमें लिया
- **Translation**: 

---

### Verse 16 (Markende Puran 0.3256)
- **Original**: चेबताओंको पीड़ा देनेबाज़ों निशुम्भकों शूल हाथंमें शक्तिसे विदोर्ण होकर कितने ही महादैत्य नष्ट हो गये। अद्याणीके मन्रपूतत जलसे निस्तेज होकर £8 3 नस #*-2
- **Translation**: 

---

### Verse 17 (Markende Puran 0.3257)
- **Original**: कितने ही भाग खडे हुए
- **Translation**: 

---

### Verse 18 (Markende Puran 0.3258)
- **Original**: कितने हो दैत्व लिब्रे आते देख चण्डिकाने वेगसे चलाये हुए अपने माहे श्ररीके त्रिशुलसे छिन्न-भिन्न हों श्रराशायों हों शूलसे उसको छाती छेद डाली
- **Translation**: 

---

### Verse 19 (Markende Puran 0.3259)
- **Original**: शूलसे विदीर्ण
- **Translation**: 

---

### Verse 20 (Markende Puran 0.3260)
- **Original**: गये। बाणाहीके थुधुनके आधातसे कितनॉका पृथ्वीपर हो जानेपर उसकी छातोसे एक टूसए महावलो एवं
- **Translation**: 

---

