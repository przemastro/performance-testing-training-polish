
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Recession](
	[YieldCurveId] [int] NULL,
	[ObservationDate] [datetime] NULL,
	[ObservationDateByMinute] [datetime] NULL,
	[Recession] [int] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[YieldCurve]    Script Date: 25.05.2019 20:49:36 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[YieldCurve](
	[Id] [int] IDENTITY(1,1) NOT NULL,
	[ObservationDate] [datetime] NULL,
	[ObservationDateByMinute] [datetime] NULL,
	[T10Y3M] [decimal](5, 2) NULL,
	[T10Y2Y] [decimal](5, 2) NULL,
PRIMARY KEY CLUSTERED 
(
	[Id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [Economy] SET  READ_WRITE 
GO
