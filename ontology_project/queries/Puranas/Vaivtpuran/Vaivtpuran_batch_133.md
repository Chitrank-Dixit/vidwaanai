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

### Verse 1 (Vaivtpuran 8.2925)
- **Original**: प्रभावसे प्रकृतिके अधिष्ठाता भगवान्‌ श्रीहरि इसे
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.6221)
- **Original**: 312 * संक्षिप्त ब्रह्म॒वैवर्तपुराण * &#%###$#$ 4454 85% 4 $ $ 5 5 # % $ % 5 # 4 5 45 5 5 5 # 5 $ % 15 # 4 $ $ 5 5 5 5 6 # # ## # %## ## 8 # # # 5 # 55 4 5 5 5 5 5 .. भक्तिपूर्वकक अतिथिका पूजन कर
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.6222)
- **Original**: भेद हैं। विद्यादाता (गुरु), अन्नदाता, भयसे रक्षा लिया, उसके द्वारा मानो भूतलपर सम्पूर्ण महादान
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.6223)
- **Original**: करनेबाला, जन्मदाता (पिता) और कन्यादाता कर लिये गये; क्‍योंकि वेदोंमें वर्णित जो नाना
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.6224)
- **Original**: (श्वशुर)--ये मनुष्योंके वेदोक्त पिता कहे गये प्रकारके पुण्य हैं, बे तथा उनके अतिरिक्त अन्य
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.6225)
- **Original**: हैं। गुरुपत्री, गर्भधात्री (जननी), स्तनदात्री पुण्यकर्म भी अतिथि-सेवाकी सोलहवीं कलाकी
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.6226)
- **Original**: (धाय), पिताकी बहिन (बूआ), माताकी बहिन समानता नहीं कर सकते। इसलिये जिसके घरसे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.6227)
- **Original**: (मौसी), माताकी सपत्नी (सौतेली माता), अन्न अतिथि अनादृत होकर लौट जाता है, उस
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.6228)
- **Original**: प्रदान करनेवाली (पाचिका) और पुत्रवधू-ये गृहस्थके पितर, देवता, अग्नि और गुरुजन भी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.6229)
- **Original**: माताएँ कहलाती हैं। भृत्य, शिष्य, दत्तक, वीर्यसे तिरस्कृत हो उस अतिथिके पीछे चले जाते हैं।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.6230)
- **Original**: उत्पन्न (औरस) और शरणागत--ये पाँच प्रकारके जो अपने अभीष्ट अतिथिकी अर्चना नहीं करता,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.6231)
- **Original**: पुत्र हैं। इनमें चार धर्मपुत्र कहलाते हैं और वह बड़े-बड़े पापोंको प्राप्त करता है। पाँचवाँ औरस पुत्र धनका भागी होता है*। माता! ब्राह्मणने कहा--वेदज्े! आप तो वेदोंके
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.6232)
- **Original**: मैं आप पुत्रहीनाका ही अनाथ पुत्र हूँ, वृद्धावस्थासे ज्ञानसे सम्पन्न हैं, अतः वेदोक्त विधिसे पूजन ग्रस्त हूँ और इस समय भूख-प्याससे पीड़ित कीजिये। माता! मैं भूख-प्याससे पीड़ित हूँ। मैंने होकर आपकी शरणमें आया हूँ। गिरिराजकिशोरी ! श्रुतियोंमें ऐसा वचन भी सुना है कि जब मनुष्य
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.6233)
- **Original**: अन्नोंमें श्रेष्ठ पूड़ी, उत्तम-उत्तम पके फल, आटेके व्याधियुक्त, आहाररहित अथवा उपवास-द्रती
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.6234)
- **Original**: बने हुए नानाप्रकारके पदार्थ, काल-देशानुसार होता है, तब वह स्वेच्छानुसार भोजन करना
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.6235)
- **Original**: उत्पन्न हुई बस्तुएँ, पक्वान्न, चावलके आटेका बना चाहता है। हुआ तिकोना पदार्थविशेष, दूध, गन्ना, गुड़के बने पार्वतीजीने पूछा--विप्रवर! आप क्या
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.6236)
- **Original**: हुए द्रव्य, घी, दही, अगहनीका भात, घृतमें पका भोजन करना चाहते हैं? बह यदि त्रिलोकीमें हुआ व्यञ्ञन, गुड़मिश्रित तिलोँके लड्डू, मेरी परम दुर्लभ होगा तो भी आज मैं आपको
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.6237)
- **Original**: जानकारीसे बाहर सुधा-तुल्य अन्य बस्तुएँ, कर्पूर खिलाऊँगी। आप मेरा जन्म सफल कीजिये।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.6238)
- **Original**: आदिसे सुवासित सुन्दर श्रेष्ठ ताम्बूल, अत्यन्त ब्राह्मणने कहा--सुब्नते! मैंने सुना है कि
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.6239)
- **Original**: निर्मल तथा स्वादिष्ट जल--इन सभी सुवासित उत्तम ब्रतपरायणा आपने पुण्यक-ब्रतमें सभी
- **Translation**: 

---

