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

### Verse 1 (Vaivtpuran 543.13394)
- **Original**: पूछा। योगीद्धोंमें श्रेष्ठ, ज्ञानियोंके गुरुके भी गुरु, आदि-
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13395)
- **Original**: हिमालय बोले--ब्रह्मन्‌! राजाधिराज अनरण्व मध्य और अन्तसे रहित, निर्विकार एवं अजन्मा
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13396)
- **Original**: किस कुलमें उत्पन्न हुए थे और उन्होंने किस परब्रह्मस्वरूप श्रीकृष्णजों बिठाकर यहाँ विवाहके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13397)
- **Original**: प्रकार अपनी पुत्री देकर समस्त सम्पदाओंकी रक्षा लिये पधारेंगें। नारायणकों साथ ले तपस्याके
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13398)
- **Original**: की थी? स्थानमें शिवने शिवाकों वर दिया है। ईध्वरकों,.. वसिष्ठजीने कहा--शैलराज ! नृपेश्वर अनरण्य दुर्लभ प्रतिज्ञा कभी विफल नहीं हो सकती।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13399)
- **Original**: मतुबंशी राजा थे। वे चिरंजीवी, धर्मात्मा, वैष्णव ब्रह्मसे लेकर कौटपर्यन्त सारा जगत्‌ नश्वर और [तथा जितेन्द्रिय थे। पहले मनुका नाम स्वायम्भुवं अस्थिर है; परंतु साधु पुरुषोंकी प्रतिज्ञा दुर्लक्वः्य
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13400)
- **Original**: है, जो ब्रह्माजीके पुत्र और अत्यन्त धर्मात्मा थे। और अमिट होती है।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13401)
- **Original**: उन्होंने इकहृत्तर चतुर्युगतक धर्मपूर्वक राज्य किया हिमालय! एक ही इन्द्रने लीलापूर्वक समस्त
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13402)
- **Original**: था। तदनन्तर वे शतरूपाके साथ वैकुण्ठधाममें पर्वतोंके पंख काट डाले । पवनदेवने खेल-खेलमें
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13403)
- **Original**: चले गये और श्रीहरिका दास्य एवं सामीप्य पाकर ही मेरु पर्वतके एक शिखरको भंग कर दिया।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13404)
- **Original**: उनके दास हो गये। तत्पश्चात्‌ स्वारोचिष मनु हुए,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13405)
- **Original**: 582 + संक्षिम्त ब्रह्मवैवर्तपुराण « 5$%$%%%%%##%##&##&##&### #ऋऋकऋ #%कऋऋऋऋऊऋऋऋऊऋऋऋ%%%%%%%
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13406)
- **Original**: ## 54 #### ########## 4 ## # #ऋ जो एक महान्‌ पुरुष थे। उनका काल व्यतीत
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13407)
- **Original**: थे। नृपश्रेष्ठ मज़़लारण्यके कोई पुत्र नहीं था; अत: हो जानेपर उत्तम मनुका राज्य आया। उत्तमके
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13408)
- **Original**: वे तपस्याके लिये पुष्करमें गये। वहाँ दीर्घकालतक भी चले जानेपर धर्मात्मा तामस मनुके पदपर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13409)
- **Original**: तप करके महेश्वरसे वर पाकर वे घर आये। वहाँ प्रतिष्ठित हुए। उनके बाद ज्ञानिशिरोमणि रैवतका
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13410)
- **Original**: उन्हें अनरण्य नामक पुत्र प्राप्त हुआ, जो भगवान्‌ मन्वन्तर आया। तत्पश्चात्‌ छठे चाक्षुप मनु और
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13411)
- **Original**: विष्णुका भक्त और जितेन्द्रिय था। उस पुत्रको सातवें श्राद्धदेव मनु उस पदके अधिकारी हुए
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13412)
- **Original**: राज्य देकर मड्भलारण्य तपस्याके लिये वनमें चले हैं। आठवें मनुका नाम सावर्णि समझना चाहिये,
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13413)
- **Original**: गये। नृपश्रेष्ठ अनरण्य सातों द्वीपोंसे युक्त पृथ्वीका जो सूर्यके ज्येष्ठ पुत्र हैं। वे ही पूर्वजन्ममें भूतलपर
- **Translation**: 

---

