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

### Verse 1 (Vishnu Puran 0.4061)
- **Original**: इस प्रकार चन्द्रदेव शुक्रपक्षमें देखताओंकों और कृष्णपक्षमें पितृगणकी पृष्टि करते हैं तथा अमृत्मय झीतल जलकणोंसे लता- वृक्षादिका और कता-ओषधि आदि उत्पन्न करके तथा अपनी चन्द्रिकाद्वारा आह्वरादित करके ते मनुष्य, पशु, एवं कीट-पतंगादि सभी प्राणियोंक्य पोषण करते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.4062)
- **Original**: चऋन्द्रमाके पुत्र खुधका रथ वायु और अग्रिमय द्रन्यका बना हुआ है और उसमें बायुके समान बेगशाली आठ पिशंग्वर्ण घोड़े जुते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.4063)
- **Original**: वरूथ", अनुकर्ष', उपासड्” और पताका तथा पृथिवीसे उत्पन्न हुए घोड़ोंके सहित शझुक्रका रथ भी अति महान्‌ है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.4064)
- **Original**: तथा मड्लका अति शोभायमान सुवर्ण-निर्मित मह्यन्‌ रथ भी अग्रिसे उत्पन्न हुए, पद्मराग-मणिके समान, अरुणवर्ण, आठ घोड़ोंसे युक्त है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.4065)
- **Original**: जो आठ पाण्डुरवर्ण घोड़ोंसे युक्त सुवर्णका रथ है उसमें बर्षके अन्तमें प्रत्येक राशिमें बृहस्पतिजी विराजमान होते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.4066)
- **Original**: आकाझसे उत्पन्न हुए जिचिज़र्ण घोड़ोंसे युक्त रथमें आरूढ़ होकर मन्दगामी शगैशरजी धीरे-धीरे चलते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.4067)
- **Original**: राहुका रथ धूसर (मटियाले) वर्णका है, उसमें भ्रमरके समान कृष्णनर्ण आट घोड़े जुते हुए है । हे मैत्रेय ! एक बार जोत दिये जानेपर वे घोड़े निरन्तर चलते रहते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.4068)
- **Original**: चन्द्रपर्वों (पूर्णिमा) पर यह राह सूर्यसे निकलकर चन्द्रमाके पास आता है तथा सौरपषवों (अमावास्था) पर यह चन्द्रमासे निकलकर सूर्यके निकट जाता है
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.4069)
- **Original**: इसो प्रकार केतुके रथके वायुबेगसाली आठ घोड़े भी पुआलके घुएँकी-सी आभावाले तथा ल्थस्कके समान लाल रड़के हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.4070)
- **Original**: है महाभाग ! मैंने तुमसे यह नवों ग्रहोंके रथॉका वर्णन किया; ये सभी वायुमयी डोरीसे धुवके साथ बैंधे हृए 1. रघकी रक्षाके लिये अना हुआ ल्जेहेका आयरण
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.4071)
- **Original**: 2. रथका नोयेका भाग । 3. शस्त्र रखनेका स्थान ।
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.4072)
- **Original**: आ> 92 ] अहर्क्षताराध्िष्ण्यानि ध्रुव बद्धान्यशेषतः । भ्रमन्त्युक्चितत्ञारेण . मैत्रेयानिलरश्मिभि:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.4073)
- **Original**: 25 यावत्त्यक्षैव तारास्तास्तावत्तो बातरइमय: । सर्वे घुबे निबद्धास्ते भ्रमन्तो भ्रामयन्ति तम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.4074)
- **Original**: 26 तैलपीडा यथा चक्र भ्रमन्तो भ्रामयन्ति वे । तथा भ्रमन्ति ज्योतीषि बातविद्धानि सर्वश:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.4075)
- **Original**: 27 अत्म्रतच्क्रवद्यान्ति बातत्रक्रेरितानि तु। यस्माज्ज्योतीषि वहति प्रबहस्तेन स स्मृत:
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.4076)
- **Original**: 28 शिशुमरारस्तु यः प्रोक्त: स ध्रुबो यत्र तिष्ठति । सन्निवेशं च॒ तस्यापषि श्ृणुत्न मुनिसत्तम
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.4077)
- **Original**: 29 बदह्ला कुरुते पापं त॑ दृष्ठा निश्चि मुच्यते । यावन्त्यश्षैव तारास्ता: शिशुमाराश्रिता दिवि। तावन्त्येव तु वर्षाणि जीवत्यभ्यधिकानि च
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.4078)
- **Original**: 30 उत्तानपादस्तस्थाधो विज्ञेयो ह्ुत्तरो हनुः। यज्ञोउ5धरश्व विज्ञेयो धर्मों मूर््धानमाश्रित:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.4079)
- **Original**: 31 हुदि नारायणश्ास्ते अश्विनौ पूर्वपादयो: । वरुणश्षार्यमा चैव पश्चिमे तस्य सक्थिनी
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.4080)
- **Original**: 32 शिक्ष: संवत्सरस्तस्थ मित्रो5पान समाश्रितः
- **Translation**: 

---

