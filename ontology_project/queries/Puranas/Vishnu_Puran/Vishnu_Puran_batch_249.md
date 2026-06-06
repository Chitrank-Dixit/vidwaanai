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

### Verse 1 (Vishnu Puran 0.4961)
- **Original**: 00 8औ0 विश किककिकककककिकककीकीिीि...... 5» &5« 5 - असम शकशिककीकीकक. 5. तृतीय अंश 277 हिरण्यनाभात्तावत्यस्संहिता . यैर्दिजोत्तमै: । इसी प्रकार जिन अन्य द्विजोत्तमोने इतनी ही संहिताएँ गृहीतास्ते5पि चोच्यन्ते पण्छितै: प्राच्यसामगा:
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4962)
- **Original**: तिरण्यनाभसे और ग्रहण की उन्हें पष्डितजन प्राच्य सामग स्परेकाक्षिनौंधमिश्षेव. कक्षोवॉन्लाडुलिस्तथा । पौष्पि्निशिष्यास्तद्ेदैस्संहिता बहुलीकृता:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4963)
- **Original**: 6 हिरण्यनाभशिष्यस्तु चतुर्विश्ञतिसंहिता: । ओ्लोवाच कृतिनामासो शिष्येभ्यश्ष महामुनिः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4964)
- **Original**: 7 तैश्वापि सामबेदोउसौ शाखाभिबहुलीकृत: । अथर्वणामथो वक्ष्ये संहितानां समुच्चयम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4965)
- **Original**: 8 अथर्वधेद॑ स॒ मुनिस्सुमन्तुरमितद्युतिः । शिष्यमध्यापयामास कब॒न्धं सो5पि त॑ द्विधा । कृत्वा तु देवदर्शाय तथा पथ्याय दत्तवान्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4966)
- **Original**: 9 देवदर्शस्य॒झ्िष्यास्तु मेधोत्रहाबलिस्तथा । शौल्कायनि: पिप्पलादस्तथान्यों द्विजसत्तम
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4967)
- **Original**: 10 पथ्यस्यापि त्रयश्श्िष्या: कृता यैर्धिज संहिता: । जाबालि: कुमुदादिक्ष तृतीयशशौनको द्विज
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4968)
- **Original**: 11 शौनकस्तु द्विधा कृत्वा ददावेकां तु बश्रवे । द्वितीयां संहितां प्रादात्सैद्यवाय च संजिने
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4969)
- **Original**: 12 सैल्ववान्युज्जिकेशश्च॒द्वेधाभिन्नाखिधा पुनः । नक्षत्रकल्पो केदानां संहितानां तथैव च
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4970)
- **Original**: 13 चतुर्थस्स्थादाड्रिसइ्शञान्तिकल्पश्च पश्चम: । श्रेष्ठास्त्वथर्वणापेते संहितानां विकल्पका:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4971)
- **Original**: 14 आख्थानैश्षाप्युपाख्यानैर्गाधाभि: कल्पशुद्धिभि: । पुराणसंहितां चक्रे पुराणार्थविशारद:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4972)
- **Original**: 15 प्रख्यातो व्यासशिष्यो5भूत्सूतो वे गेमहर्षण: । कहते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4973)
- **Original**: पौष्पिज्ञिके शिष्य स्त्रेकाक्षि, नौधमि, कशक्षीवान्‌ और लांगलि थे। उनके हिष्य-प्रश्चिष्योने अपनी-अपनी संहिताओंके विभाग करके उन्हें बहुत बढ़ा दिया
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4974)
- **Original**: महामुनि कृति नामक हिरण्यनाभके एक और जिष्यने अपने शिष्योंको सामवेदकी चौबीस संहिताएँ पढ़ायीं
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4975)
- **Original**: फिर उन्‍होंने भी इस सामवेदका शाखाओंद्वारा स्बृब विस्तार किया । अब मैं अथर्ववेदकी सेहिताओंके समुश्य्का वर्णन करता हूँ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4976)
- **Original**: अधर्ववेदफको सर्वप्रथम अमिततेजोमय सुमसन्तु मुनिने अपने दिष्य कबन्धव्मे पढ़ाया था फिर कबन्धने उसके दो भाग कर उन्हें देवदर्श और पथ्य नामक अपने दिष्योंको दिया
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4977)
- **Original**: हे ट्विजसत्तम ! देवदर्शके शिष्य मेथ, बह्यबल्ति, शौल्कायनि और पिपष्पछ थे
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4978)
- **Original**: है द्विज ! पथ्यके भी जाबालि, कुमुदांदि और शौनक नामक तीन दिष्य थे, जिन्होंने संहिताओंका तिभाग किया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4979)
- **Original**: शौनकने भी अपनी संहिताके दो विभाग करके उनमेंसे एक वप्रुको तथा दूसरी सैन्घब नामक अपने श्िष्यको दो
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4980)
- **Original**: सैन्क्‍बसे पढ़कर मुझिकेशने अपनी संहिताके पहले दो और फिर तीन [ इस प्रकार पाँच ] विभाग किये। नक्षजकल्प, वेदकल्प, संहिताकल्प, आगिस्सकल्प और शान्तिकल्प--उनके रखे हुए ये पाँच खिकलल्‍्प अधर्वलेद-संहिताओंमें सर्वश्रेष्ठ हैं
- **Translation**: 

---

