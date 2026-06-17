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

### Verse 1 (Vaivtpuran 8.2825)
- **Original**: झाँकीको देखकर गज्जाका मन तृप्त न हो सका। राधासे कुशल पूछी। थे डरकर नीचे खड़ी हो
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.2826)
- **Original**: बे निर्निमेष नेत्रोंसे निरन्तर राधा-सौन्दर्य-सुधाका गयीं। उन्होंने ध्यानके द्वारा मन-ही-मन श्रीकृष्णके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.2827)
- **Original**: पान करती रहीं। मुने ! इतनेमें राधाने मधुर वाणीमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.2828)
- **Original**: जगदीश्वर भगवान्‌ श्रीकृष्णससे कहा। उस समय
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.2829)
- **Original**: जगह बाँट दिया। श्रीकृष्ण! आपको आँखोंसे दूर श्रीराधाका विग्रह परम शान्त था। उनमें नम्नता हुई प्रभा अग्रि, यक्ष, नरेश, देवता, वैष्णवजन, आ गयी थी और उनके मुखपर मुस्कान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.2830)
- **Original**: नाग, ब्राह्मण, मुनि, तपस्वी, सौभाग्यवती स्त्री छायी थी। तथा यशस्वी पुरुष-इन सबको थोड़े-थोड़े श्रीराधाने कहा--प्राणेश! आपके प्रसन्न
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.2831)
- **Original**: रूपोंमें प्राप्त हुई। मुखकमलको मुस्कराकर निहारनेवाली यह कल्याणी एक बार मैंने आपको 'शान्ति' नामक कौन है? इसके तिरछे नेत्र आपको लक्ष्य कर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.2832)
- **Original**: गोपीके साथ रासमण्डलमें प्रेम करते देखा था। रहे हैं। इसके भीतर मिलनेच्छाका भाव जाग्रतू
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.2833)
- **Original**: प्रभो! वह शान्ति भी अपने उस शरीरकों छोड़कर है। आपके मनोहर रूपने इसे अचेत कर दिया
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.2834)
- **Original**: आपमें लीन हो गयी। उस समय उसका शरीर है। इसके सर्वाड्र पुलकित हो रहे हैं। वस्त्रसे उत्तम गुणके रूपमें परिणत हो गया। तदनन्तर मुख ढँककर बार-बार आपको देखा करना मानो । आपने उसको विभाजित करके विश्वमें बाँट दिया। इसका स्वभाव ही बन गया है। आप भी उसकी
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.2835)
- **Original**: प्रभो! उसका कुछ अंश मुझ (राधा)-में, कुछ ओर दृष्टिपात करके मधुर-मधुर हँस रहे हैं। आप
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.2836)
- **Original**: इस निकुज्ञमें और कुछ ब्राह्मणमें प्राप्त हुआ। अनेक बार ऐसा करते हैं और कोमल-स्वभावकी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.2837)
- **Original**: विभो! फिर आपने उसका कुछ भाग शुद्ध स्त्री-जाति होनेके कारण प्रेमवश मैं क्षमा कर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.2838)
- **Original**: सत्त्वस्वरूपा लक्ष्मीको, कुछ अपने मन्त्रके देती हूँ। उपासकोंको, कुछ वैष्णवोंको, कुछ तपस्वियोंको, आपने “विरजा' (रजोगुणरहिता देवी)- से [कुछ धर्मको और कुछ धर्मात्मा पुरुषोंकों सौंप प्रेम किया। फिर वह अपना शरीर त्यागकर महान्‌
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.2839)
- **Original**: दिया। नदीके रूपमें परिणत हो गयी। आपकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.2840)
- **Original**: पूर्वसमयकी बात है, “क्षमा'के साथ आप सत्कौर्तिस्वरूपिणी वह देवी नदीरूपमें अब भी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.2841)
- **Original**: मुझे प्रेम करते दृष्टिगोचर हुए थे। उस समय विराजमान है। आपके औरस पुत्रके रूपमें उससे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.2842)
- **Original**: क्षमा अपना बह शरीर त्यागकर पृथ्वीपर चली समवानुसार सात समुद्र उत्पन्न हो गये। प्राणनाथ !
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.2843)
- **Original**: गयी। तदनन्तर उसका शरीर उत्तम गुणके रूपमें आपने 'शोभा'से प्रेम किया। वह भी शरीर
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.2844)
- **Original**: परिणत हो गया था। फिर उसके शरीरका आपने त्यागकर चद्रमण्डलमें चली गयीं। तदनन्तर
- **Translation**: 

---

