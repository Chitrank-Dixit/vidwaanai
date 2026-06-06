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

### Verse 1 (Vaivtpuran 13.10622)
- **Original**: हो गये हैं। जो जिसका सदा ध्यान करता है, परिमाण वही है, जो बेदोंमें बताया गया है। एक
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10623)
- **Original**: वह निश्चय ही उसे प्राप्त कर लेता है। इतना हजार बैल हों और उनके सौंगोंमें सोना मढ़ा गया
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10624)
- **Original**: ही नहीं-ध्याता पुरुष गुण, तेज, बुद्धि और हो। ब्रह्मन्‌! इस प्रकार 'त्रैमासिक' व्रत बताया
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10625)
- **Original**: ज्ञानको दृष्टिसे अपने ध्येयके समान ही हो जाता गया। इस ब्रतका अनुष्ठान कर लिया जाय तो
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10626)
- **Original**: है। श्रीकृष्णके चिन्तन, तप, ध्यान और सेवासे यह विशिष्ट संतति देनेवाला और पतिसौभाग्यकी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10627)
- **Original**: मैंने आप-जैसा स्वामी और पुत्र भी प्राप्त किया वृद्धि करनेवाला होता है। इस ब्रतके प्रभावसे सौ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10628)
- **Original**: है। मुझे अनायास ही सब कुछ मिल गया। मेरा जन्मोंतक नारीका अखण्ड सौभाग्य बना रहता है
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10629)
- **Original**: मनोरथ पूर्ण हो गया। मुझे आप-जैसे स्वामी और निश्चय ही वह सौ जन्मोंतक सत्पुत्रकी जननी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10630)
- **Original**: मिले। कार्तिकय और गणेश-जैसे पुत्र प्राप्त हुए होती है। उसका कभी पति और पुत्रसे वियोग
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10631)
- **Original**: तथा श्रीकृष्णके अंशस्वरूप हिमवान्‌-जैसे पिता नहीं होता। पुत्र दासकी भाँति उसकी आज्ञाका
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10632)
- **Original**: मिले। प्रभो! मेरे लिये कौन-सी वस्तु दुर्लभ है? पालक होता है तथा पति भी उसकी बातकों
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10633)
- **Original**: पार्वतीकी यह बात सुनकर भगवान्‌ शंकर माननेवाला होता है। वह सती नारी प्रतिक्षण
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10634)
- **Original**: बहुत प्रसन्न हुए। उनका शरीर पुलकित हो उठा श्रीराधा-कृष्णकी भक्तिसे सम्पन्न होती है। ब्रतके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10635)
- **Original**: और वे हँसकर मधुर वाणीमें बोले। प्रभावसे उसको ज्ञान तथा श्रीहरिकी स्मृति प्राप्त श्रीमहादेवजीने कहा--ईश्वरि! तुम होती है। इस सामवेदोक्त व्रतका पूर्वकालमें हम
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10636)
- **Original**: महालक्ष्मीस्वरूपा हो। तुम्हारे लिये क्या असाध्य दोनोंने भी पालन किया था। ब्रह्मन्‌! दूसरी है? तुम सर्वसम्पत्स्वरूपा और अनन्तशक्तिरूपिणी स्त्रियोंद्रा उस व्रतका अनुष्ठान होता देख पार्वतीदेवीने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10637)
- **Original**: हो। देवि! तुम जिसके घरमें हो, बह सम्पूर्ण प्रसन्नतापूर्वक दोनों हाथ जोड़ भक्तिभावसे सिर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10638)
- **Original**: ऐश्वर्यका भाजन है। शुभप्रदे ! मैं, ब्रह्मा और विष्णु झुकाकर भगवान्‌ शंकरसे कहा। तुममें भक्ति रखकर तुम्हारे कृपाप्रसादसे ही पार्वती बोलीं--जगन्नाथ! आज्ञा कीजिये।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10639)
- **Original**: संसारकी सृष्टि, पालन और संहारमें समर्थ हुए मैं उत्तम ब्रतका पालन करूँगी। हम दोनोंके हैं। हिमालय कौन है? मेरी क्‍या बिसात है
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10640)
- **Original**: * श्रीकृष्णजन्मखण्ड * ड75 4#08£#% 84% 5 ऋ$% 45 4 5 8 5 # 44% 8 5 4 4 5 8 % ऋ% % 45 4 % 4 $ $# 9 5/ 4989 $# 5 9885 98 89 4 9986 45 98 8 98 88 8 #_ और कार्तिकेय तथा गणेश क्‍या हैं ? तुम्हारे बिना
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10641)
- **Original**: किया। नारद! इस प्रकार पार्वतीजीने जो ब्रत हम सब लोग असमर्थ हैं और तुम्हारा सहयोग
- **Translation**: 

---

