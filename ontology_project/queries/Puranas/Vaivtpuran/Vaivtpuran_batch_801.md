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

### Verse 1 (Vaivtpuran 543.14334)
- **Original**: (62। 21-23)
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14335)
- **Original**: रन्‍म>««»म>-_«म>»» अमान". द । __ रे कापरैयपराणा 5. £*5%%ऋ%%$# # # #% 5 %$$## 8 ## 65% 55% 4 #### 666 #####&########### 55 यश, प्रतिष्ठा, प्रताप और परम आदरकौ प्राप्ति
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14336)
- **Original**: बातचीत हुई। अन्तमें लक्ष्मणने तीक्ष्ण धारवाले होती है*। मैं चौदह_ वर्षोतक गृह-सुखका अर्धचन्द्राकार बाणसे उसकौ नाक काट ली। परित्याग करके धर्मपूर्वक विचरता हुआ आपके
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14337)
- **Original**: उसका भाई खर-दूषण बड़ा बलबवान्‌ था। उसने सत्यकी रक्षाके लिये वनमें वास करूँगा। जो
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14338)
- **Original**: आकर बुद्ध किया और लक्ष्मणके अस्त्रसे इच्छा या अनिच्छासे सत्य प्रतिज्ञा करके उसका
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14339)
- **Original**: सेनासहित मारा जाकर यमलोकको चला गया। पालन नहीं करता, वह अशौचका भागी होता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14340)
- **Original**: चौदह हजार राक्षसों तथा खर-दूषणको मारा गया है और वह अशौच उसके शरीरके भस्म होनेतक
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14341)
- **Original**: देख शूर्पणखाने रावणकों फटकारा और सारा बना रहता है। जबतक चन्द्रमा और सूर्य रहते
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14342)
- **Original**: समाचार बताकर वह तत्काल पुष्करतीर्थमें चली हैं, तबतक वह कुम्भीपाक नरकमें यातना भोगता
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14343)
- **Original**: गयी। वहाँ दुष्कर तपस्या करके उसने ब्रह्माजीसे है। तदनन्तर मानब-योनिमें उत्पन्न हो वह सात
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14344)
- **Original**: वर प्राप्त किया। उस निराहार-तपस्विनी राक्षसीको जन्मोंतक गूँगा और कोढ़ी होता है। दर्शन देकर सर्वज्ञ कृपासिन्धु ब्रह्माजीने उसके ऐसा कहकर श्रीराम वल्कल और जटा
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14345)
- **Original**: मनकी बात जान ली और इस प्रकार कहा। धारण करके सीता और लक्ष्मणके साथ विशाल
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14346)
- **Original**: ब्रह्माजी बोले--वरानने ! श्रीराम दुर्लभ हैं। बनमें चले गये। मुने! इधर महाराज दशरथने [उन्हें तुम प्राप्त नहीं कर सकी हो। इसीलिये पुत्रशोकसे अपने शरीरको त्याग दिया। श्रीरामचन्द्रजी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14347)
- **Original**: यह दुष्कर तपस्या कर रही हो। इसी तरह पिताके सत्यको रक्षाके लिये बन-वनमें भ्रमण
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14348)
- **Original**: जितेन्द्रियोंमें श्रेष्ठ धर्मात्मा लक्ष्मणको भी प्राप्त करने लगे। कालान्तरमें उस बिशाल एवं घोर
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14349)
- **Original**: करनेमें तुम्हें सफलता नहीं मिली है; अतः वनमें घूमती हुई रावणकी बहिन शूर्पणखा उधर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14350)
- **Original**: उधरसे निराश होकर तुम तपस्यामें लगी हो। आ निकली। उसने बड़े कौतूहलसे श्रीरामको
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14351)
- **Original**: तुम्हारी इस तपस्याका फल तुम्हें दूसरे जन्ममें देखा। उन्हें देखते ही वह कुलटा राक्षसी काम- , मिलेगा। जो ब्रह्मा, विष्णु और शिव आदिके बेदनासे पीड़ित हो गयी। उसके सारे अज्जोंमें भी ईश्वर तथा प्रकृतिसे भी परे हैं, उन भगवान्‌ रोमाझ्न हो आया और वह मूर्च्छित हो गयी।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14352)
- **Original**: श्रीकृष्णनों तुम पतिरूपमें प्राप्त करोगी। फिर बह श्रीरामके पास गयी। शूर्पणखा सदा ऐसा कहकर ब्रह्माजी सानन्द अपने बने रहनेबाले यौवनसे युक्त, अत्यन्त प्रौ़ और
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14353)
- **Original**: धामकों चले गये और शूर्पणखाने अपने कम कप थी। वह मनमें कामभाव ले श्रीरामसे
- **Translation**: 

---

