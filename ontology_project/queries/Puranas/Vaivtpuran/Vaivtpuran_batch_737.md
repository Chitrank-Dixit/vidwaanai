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

### Verse 1 (Vaivtpuran 543.13054)
- **Original**: यौवनका गर्व त्याग दिया। अब उन्हें सखियोंको परमात्मा शिवपर जब वह शस्त्र विफल हो गया,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13055)
- **Original**: अपना मुँह दिखानेमें भी लज्जाका अनुभव होने तब कामदेवको बड़ा भय हुआ। वह सामने खड़ा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13056)
- **Original**: लगा। सब देवता रतिको आश्वासन दे रुद्रदेवको हो भगवान्‌ मृत्युझ्बकी ओर देखता हुआ काँपने
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13057)
- **Original**: दण्डवत्‌ प्रणाम करनेके पश्चात्‌ अपने स्थानको लगा। भयसे विह्लल हुए कामने इन्द्र आदि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13058)
- **Original**: चले गये। उस समय उनका मन शोकसे उ्ठिग्र देवताओंका स्मरण किया। तब सब देवता वहाँ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13059)
- **Original**: हो रहा था। राधिके! कामपत्नी रति रोषसे लाल आये और शंकरके कोपसे डरकर काँपने लगे।
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13060)
- **Original**: आँखोंवाले रुद्रदेवका भयसे स्तवन करके शोकसे उन्होंने स्तोत्र पढ़कर देवाधिदेव शंकरका स्तवन
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13061)
- **Original**: रोती हुई अपने घरको चली गयी। परंतु पार्वती किया। इतनेमें ही शिवके ललाटवर्ती नेत्रसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13062)
- **Original**: लज्जावश पिताके घर नहीं गयी। वह सखियोंके कोपाग्नि प्रकट हुईं। देवतालोग स्तुति कर ही
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13063)
- **Original**: मना करनेपर भी तपस्याके लिये बनमें चली रहे थे कि शम्भुसे उत्पन्न हुई बह आग ऊँची-
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13064)
- **Original**: गयी। तब शोकसे विह्ल हुई सखियोंने भी ऊँची लपटें उठाती हुई प्रज्वलित हो उठी। वह
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13065)
- **Original**: उन्हींका अनुगमन किया। माताओंके रोकनेपर भी प्रलयकालिक अग्निकी ज्वालाके समान जान
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13066)
- **Original**: वे सब-कौ-सब गड्भातटवर्ती वनकी ओर चली
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13067)
- **Original**: 570 * संक्षिप्त ब्रह्मवैयर्तपुराण * कक ##
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13068)
- **Original**: #8#$%$%%%$ऊ$########%$%5$55ऊऊऋछक़क्क््##&###कक्ककऋकऋऋऋशड कद ड्कहक #ऋ कक ऋऋऋऋ कक क गयीं। आगे चलकर पार्वतीने दीर्घकालतक
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13069)
- **Original**: दर्पमोचनसे सम्बन्ध रखनेवाली सारी बातें कही तपस्या करके भगवान्‌ त्रिलोचनको पतिरूपमें प्राप्त
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13070)
- **Original**: गयीं। पार्वतीका यह चरित्र गूढ़ है। बताओ, तुम किया। रतिने भी शंकरके वरसे यथासमय
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13071)
- **Original**: और क्या सुनना चाहती हो? कामदेबको प्राप्त किया। राधे ! इस प्रकार पार्वतीके (अध्याय 39) #44> मद 0-0>0 पार्वतीकी तपस्या, उनके तपके प्रभावसे अग्निका शीतल होना, ब्राह्मण-बालकका रूप धारण करके आये हुए शिवके साथ उनकी बातचीत, पार्वतीका घरको लौटना और माता-पिता आदिके द्वारा उनका सत्कार, भिक्षुवेषधारी शंकरका आगमन, शैलराजको उनके विविध रूपोंके दर्शन, उनकी शिव-भक्तिसे देवताओंको चिन्ता, उनका बृहस्पतिजीको शिव-निन्दाके लिये उकसाना तथा बृहस्पतिका देवताओंको शिव-निन्दाके दोष बताकर तपस्याके लिये जाना श्रीराधिका बोलीं--प्रभो! यह बहुत ही
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13072)
- **Original**: निराहार रहकर भक्ति-भावसे तपस्या की। तदनन्तर विचित्र और अपूर्व चरित्र सुननेको मिला है, और भी कठोर तप आरम्भ किया। ग्रीष्म-ऋतुमें जो कानोंमें अमृतके समान मधुर, सुन्दर, निगृढ़
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13073)
- **Original**: अपने चारों ओर आग प्रज्वलित करके वह दिन- एवं ज्ञानका कारण है। भगवन्‌ ! यह न तो अधिक
- **Translation**: 

---

