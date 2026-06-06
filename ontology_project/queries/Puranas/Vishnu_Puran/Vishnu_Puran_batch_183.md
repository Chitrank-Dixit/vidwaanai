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

### Verse 1 (Vishnu Puran 0.3641)
- **Original**: 12 श्रीपराशरजी ओले--हे सुब्रत ! मैने तुमसे यह ब्रह्माण्डकी स्थिति कही, अय सूर्य आदि ग्रहोंकी स्थिति और उनके परिमाण सुनो
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3642)
- **Original**: हे मुनिश्रेष्ठ ! सूर्यदेवक्े रथका लिस्तार नौ हजार योजन है तथा इससे दूना उसका ईषा-दण्ड (जुआ ओर रथके बीचका भाग) है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3643)
- **Original**: उसका धुरा डेढ़ करोड़ सात लाख योजन लम्ना है जिसमें उसका पहिया लगा हुआ है
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3644)
- **Original**: उस पूर्वाह्न, मध्याह्ल और पराह्करूप तीन नाभि, परिवत्सरादि पाँच अरे और घड्‌-ऋतुरूप छः नेमिवाक्े अक्षयस्वरूप संवत्सरात्मक चक्रमें सम्पूर्ण कालचक्र स्थित है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3645)
- **Original**: सात छन्द ही उसके घोड़े हैं, उनके नाम सुनो--गायत्री, बृठत्ी, उच्णिक्‌, जगती, त्रिष्टप, अनुष्टप्‌ और पंक्ति--ये छन्‍्द ही सूर्यके सात घोड़े कहे गये हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3646)
- **Original**: हे महामते ! भगनान सूर्यके रथका दूसरा धुण साढ़े पैतालीस सहस्त योजन लम्बा है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3647)
- **Original**: दोनों धुरॉंके परिमाणके तुल्य हो उसके युगाद्धों (जूओं) का परिमाण है, इनमेंसे छोटा धुरा उस रथके एक युगार्द (जुए) के सहित धुक्के आधारपर स्थित है और दूसरे घुरेका चक्र मानसोत्तरपर्वतपर स्थित है
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3648)
- **Original**: इस मानसोत्तरपर्वतके पूर्वमें इन्द्रकी, दक्षिणमें यमको, पश्चिममें बरुणकी और उत्तरमें चन्द्रमावत्री पुरी है; उन प्रियोंके नाम सुनो
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3649)
- **Original**: इन्द्रकी पुरी बस्वौकसारा है, यमकी संयमनी है, वरुणक सुख्ता है तथा चन्द्रमाकी विभावरी है
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3650)
- **Original**: हे मैत्रेय
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3651)
- **Original**: ! ज्योतिश्रक्रके सहित भगबान्‌ भानु दक्षिण-दिश्यामें प्रवेशकर छोड़े हुए बाणके समान तीव सेगसे चलते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3652)
- **Original**: भगवान सूर्यदेव दिन और रात्रिकरी व्यवस्थाके कारण हैं और रागादि फ्ैशॉकि क्षीण हो जानेपर वे ही क्रममुक्तिभागी योगिजनोंके देक्यान नामक श्रेष्ठ मार्ग हैं
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3653)
- **Original**: हे मैत्रेय ! सभी द्रीपॉमें सर्वदा मध्याह् तथा मध्यरात्रिके समय सूुर्यदित मध्य-आकाशार्में सामनेकी ओर रहते हैं*
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3654)
- **Original**: * अर्थात्‌ जिस द्वीप या खण्डमें सूर्यदेव सध्याह्के समय सम्मुख पड़ते हैं उसकी समान रेखापर दूसरी ओर स्थित द्वीपान्तरसें जे उसी प्रकार मध्यरात्रिके समय रहते हैं।
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3655)
- **Original**: 130 130 ॒_॒_॒__॒_॒_॒_॒_॒ शअ्रीविष्यपुण
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3656)
- **Original**: ैुऋ"तचतृ्॒ूझ आअःट8 [ अर 8 उदयास्तमने चैव सर्वकालं तु सम्मुखे। विदिशासु त्वशेषासु तथा ब्रह्मन्‌ दिशासु च
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3657)
- **Original**: 13 यैर्थत्र दृश्यते भास्वान्स तेषामुदयः स्मृतः । तिरोभाव॑ च यत्रैति तप्रैवास्तमन॑ रवे:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3658)
- **Original**: 14 नैवास्तमनमर्कस्थ नोदय: सर्वदा सतः। उदयास्तमनाख्य॑ हि दर्शनादर्शन॑ रवे:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3659)
- **Original**: 15 शक्रादीनां पुरे तिष्ठन्‌ स्पृशत्येष पुरत्रयम्‌। बिकोणों ड्ो विकोणस्थस््रीन्‌ कोणान्द्रे पुरे तथा
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3660)
- **Original**: 16 उदितो वर्द्धमानाभिरामध्याद्वात्तपन्नवि: । ततः पर हुसन्तीभिगोभिरस्त नियच्छति
- **Translation**: 

---

