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

### Verse 1 (Vishnu Puran 0.6261)
- **Original**: है प्विजश्रेष्ट इस प्रकार शुद्ध हो जानेपर उसने 5 “10040 4 स्वर्ग, अति दुर्लभ दाम्पत्य और अपने पूर्वार्जित फल प्राप्त कर लिया
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6262)
- **Original**: हे ट्विज ! इस प्रकार गैंने तुमसे पासष्डीसे सम्माषण करतेका दोष और अप्नमेध-यज्ञमें स्रान करनेका माहारुय वर्णन कर दिया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6263)
- **Original**: इसलिये पाखण्डी और पापाचारियोंसे कभी वार्तात्मप और स्पर्श न करे; विशेषतः नित्य-नैमित्तिक कमेकि समय और जो यज्ञादि क्रियाओंके छिये दीक्षित हो उसे तो उनका संसर्ग त्यागना अस्यन्त आवश्यक है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6264)
- **Original**: जिसके घरमें एक मासतक नित्यकर्मोका अनुष्ठान न हुआ हो उसको देख लेनेपर प्रनुष्य सूर्यका दर्शन करे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6265)
- **Original**: फिर जिन्होंने तथा जो पासण्डियोंका अन्न खाते और वैदिक मतका विरोध करते हैं उन पापात्माओंके दर्शनादि करनेपर तो कहना ही क्या है ?
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6266)
- **Original**: इन दुराचारी साथ वबार्ताल्ाप रखने और उठने-बैठनेमें महान्‌ पाप होता है; इसलिये इन सब बातोंका त्याग करें
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6267)
- **Original**: पाखण्डी, किकर्मी, विड्ाल-ब्रतवाले,* दुष्ट, स्वार्थी और यगुर्प्-भक्त ल्मेणोंक्ा वाणीसे भी आदर न करे
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6268)
- **Original**: इन पाशप्डी, दुगचारी और अति पापियोंका संसर्ग टूरहीसे त्यागने योग्य है। इसछिसये इनका सर्व॑दा व्थाग करे
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6269)
- **Original**: इस प्रकार मैंने तुमसे नम्रोंकी व्याख्या की, जिनके दर्बानमात्रसे श्राद्ध नष्ट हो जाता है और जिनके साथ सम्भाषण करनेसे मनुष्यका एक 8 झ्लीण हो जाता है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6270)
- **Original**: ये पाखण्डो बड़े पापी होते सम्पाषण न करे। इनके साथ सम्भाषण उस दिनका पुण्य नष्ट हो जाता हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6271)
- **Original**: जो बिन्न कारण ही जटा धारण करते अथवा एूँड़॒ मुड़ाते हैं, देवता, अतिथि आदिक्ध भोजन कराये बिना खयं ही भोजन कर छेते हैं, सब प्रकारसे शौचहीन हैं तथा जल-दान और पितृ-पिण्ड आदिसे भी बहिष्कृत हैं, उन सम्भाषणादपि नशा नरक प्रयात्ति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6272)
- **Original**: 105 [ स्नेगॉंसे वार्ताराप करनेसे भी लोग नरकमें जाते हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6273)
- **Original**: इति श्रीविष्णुपुराणे तृतीयें5शे अष्टादशोउ्ध्याय:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6274)
- **Original**: इति श्रीविष्णुपरत्वनिर्णायके श्रीमति विष्णुमहापुराणे तृतीयोंड्शा: समाप्त: । धिा + 'प्रच्छन्नानि च पापानि वैडाल॑ नाम तदब़म्‌ अर्थात्‌ छिपे-छिपे पाप करना चैडाल नामक व॒त है। जो लैसा करते हैं 'बे बिदास-ब्रतबाले” कहत्मते हैं।
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6275)
- **Original**: छः 2-5 जे कक ध््््् न््ज््् ्ज््ड्ड 33
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6276)
- **Original**: 447 लि 5 ््य्य््् न धर स््् जज 6// । 222 जज कै जय 4 रह औ%उ 0» हह अल >>
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6277)
- **Original**: डे अआमज्ाराबणाय श्रीविष्णुपुराण जज शऔै- चतुर्थ अंश व फ्र 0 पहला अध्याय खैवस्वतमनुके वंचाका विवरण श्रीमैत्रेय उकच भगवन्यन्नरैः कार्य साथुकर्मण्यवस्थितै: । तन्महां गुरुणाख्यातं नित्यनैमित्तिकात्मकम्‌
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6278)
- **Original**: 1 वर्णधर्मास्तथाख्याता धर्मा ये चाश्रमेषु चर । श्रोतुमिच्छाम्यहं वंश राज्ञां तद्‌ ब्रूहि मे गुरो
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6279)
- **Original**: 2 श्रोपरासर उवाच मैत्रेय श्रूयतामयमनेकयज्वशूरवी रधीरभूपाला - लड्डुतो ब्रह्मादिमानवो वंश:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6280)
- **Original**: टला कथां श्रृूणु
- **Translation**: 

---

